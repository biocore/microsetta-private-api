import psycopg2
import datetime

from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.source import Source, HumanInfo, NonHumanInfo

from werkzeug.exceptions import NotFound
from hashlib import sha512


def _source_to_row(s):
    d = s.source_data
    row = (s.id,
           s.account_id,
           s.source_type,
           s.name,
           getattr(d, 'email', None),
           getattr(d, 'is_juvenile', None),
           getattr(d, 'parent1_name', None),
           getattr(d, 'parent2_name', None),
           getattr(d, 'deceased_parent', None),
           getattr(d, 'consent_date', None),
           getattr(d, 'date_revoked', None),
           getattr(d, 'assent_obtainer', None),
           getattr(d, 'age_range', None),
           getattr(d, 'description', None))
    return row


def _row_to_human_info(r):
    return HumanInfo(
        r['participant_email'],
        r['is_juvenile'],
        r['parent_1_name'],
        r['parent_2_name'],
        r['deceased_parent'],
        r['date_signed'],
        r['date_revoked'],
        r['assent_obtainer'],
        r['age_range'])


def _row_to_nonhuman_info(r):
    return NonHumanInfo(r["description"])


row_to_obj_funcs_by_type = {
    Source.SOURCE_TYPE_HUMAN: _row_to_human_info,
    Source.SOURCE_TYPE_ANIMAL: _row_to_nonhuman_info,
    Source.SOURCE_TYPE_ENVIRONMENT: _row_to_nonhuman_info
}


def _row_to_source(r):
    row_to_obj = row_to_obj_funcs_by_type[
        r['source_type']]
    return Source(r[0], r[1], r[2], r[3], row_to_obj(r))


# Note: By convention, this references sources by both account_id AND source_id
# This should make it more difficult to accidentally muck up sources when the
# user doesn't have the right permissions
class SourceRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    read_cols = "id, account_id, " \
                "source_type, source_name, participant_email, " \
                "is_juvenile, parent_1_name, parent_2_name, " \
                "deceased_parent, date_signed, date_revoked, " \
                "assent_obtainer, age_range, description, " \
                "creation_time, update_time"

    write_cols = "id, account_id, source_type, " \
                 "source_name, participant_email, " \
                 "is_juvenile, parent_1_name, parent_2_name, " \
                 "deceased_parent, date_signed, date_revoked, " \
                 "assent_obtainer, age_range, description"

    def get_sources_in_account(self, account_id, source_type=None,
                               allow_revoked=False):
        if not allow_revoked:
            no_revoked = " AND source.date_revoked IS NULL"
        else:
            no_revoked = ""

        with self._transaction.dict_cursor() as cur:
            if source_type is None:
                cur.execute("SELECT " + SourceRepo.read_cols + " FROM "
                            "source "
                            "WHERE "
                            "source.account_id = %s" + no_revoked,
                            (account_id,))
            else:
                cur.execute("SELECT " + SourceRepo.read_cols + " FROM "
                            "source "
                            "WHERE "
                            "source.account_id = %s AND "
                            "source.source_type = %s" + no_revoked,
                            (account_id, source_type))

            rows = cur.fetchall()
            return [_row_to_source(x) for x in rows]

    def get_source(self, account_id, source_id, allow_revoked=False):
        if not allow_revoked:
            no_revoked = " AND source.date_revoked IS NULL"
        else:
            no_revoked = ""

        with self._transaction.dict_cursor() as cur:
            cur.execute("SELECT " + SourceRepo.read_cols + " FROM "
                        "source "
                        "WHERE "
                        "source.id = %s AND "
                        "source.account_id = %s" + no_revoked,
                        (source_id, account_id))
            r = cur.fetchone()
            if r is None:
                return None
            return _row_to_source(r)

    def update_source_data_api_fields(self, source):
        # Business Policy: For now I will let them edit only name and
        # description.  Anything else they have to recreate the source
        # Everything else they send up, we currently ignore.
        # TODO: Change yaml to remove extraneous fields?
        #  Raise exc in this layer?

        with self._transaction.cursor() as cur:
            cur.execute("UPDATE source "
                        "SET "
                        "source_name = %s, "
                        "description = %s "
                        "WHERE "
                        "source.id = %s AND "
                        "source.account_id = %s",
                        (
                            getattr(source, 'name', None),
                            getattr(source.source_data, 'description', None),
                            source.id,
                            source.account_id
                        )
                        )
            return cur.rowcount == 1

    def create_source(self, source):
        with self._transaction.cursor() as cur:
            acct_repo = AccountRepo(self._transaction)
            if acct_repo.get_account(source.account_id) is None:
                raise NotFound("No such account_id")

            cur.execute("INSERT INTO source (" + SourceRepo.write_cols + ") "
                        "VALUES("
                        "%s, %s, %s, "
                        "%s, %s, "
                        "%s, %s, %s, "
                        "%s, %s, %s, "
                        "%s, %s, %s)",
                        _source_to_row(source))

            host_subject_id = self.construct_host_subject_id(source.account_id,
                                                             source.name)
            cur.execute("""INSERT INTO source_host_subject_id (source_id,
                                                               host_subject_id)
                           VALUES (%s, %s)""",
                        (source.id, host_subject_id))

            return cur.rowcount == 1

    @staticmethod
    def construct_host_subject_id(account_id, source_name):
        prehash = account_id + source_name.lower()
        return sha512(prehash.encode()).hexdigest()

    def get_host_subject_id(self, source):
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT host_subject_id
                           FROM source_host_subject_id
                           WHERE source_id = %s""",
                        (source.id, ))
            r = cur.fetchone()
            if r is None:
                return None
            return r

    def delete_source(self, account_id, source_id):
        try:
            with self._transaction.cursor() as cur:
                cur.execute("DELETE FROM source_host_subject_id "
                            "WHERE source_id = %s",
                            (source_id, ))
                cur.execute("DELETE FROM source WHERE source.id = %s AND "
                            "source.account_id = %s",
                            (source_id, account_id))
                return cur.rowcount == 1
        except psycopg2.errors.ForeignKeyViolation as e:
            if e.diag.constraint_name == "fk_ag_kit_barcodes_sources":
                raise RepoException("A source cannot be deleted while samples "
                                    "are associated with it") from e
            raise RepoException("Error deleting source") from e

    def scrub(self, account_id, source_id):
        """Replace identifying information with scrubbed text

        Parameters
        ----------
        account_id : str, uuid
            The associated account ID to scrub
        source_id : str, uuid
            The associated source ID to scrub

        Raises
        ------
        RepoException
            If the source was not found
            If the source is not human
            If the update failed

        Returns
        -------
        True if the record was updated, raises otherwise
        """
        source = self.get_source(account_id, source_id)

        if source is None:
            raise RepoException("Source not found")

        if source.source_type != Source.SOURCE_TYPE_HUMAN:
            raise RepoException("Source is not human")

        name = "scrubbed"
        description = "scrubbed"
        email = "scrubbed@microsetta.ucsd.edu"
        parent1_name = "scrubbed"
        parent2_name = "scrubbed"
        assent_obtainer = "scrubbed"
        date_revoked = datetime.datetime.now()

        with self._transaction.cursor() as cur:
            cur.execute("""UPDATE source
                           SET source_name = %s,
                               participant_email = %s,
                               description = %s,
                               parent_1_name = %s,
                               parent_2_name = %s,
                               date_revoked = %s,
                               assent_obtainer = %s,
                               update_time = %s
                           WHERE id = %s""",
                        (name, email, description, parent1_name, parent2_name,
                         date_revoked, assent_obtainer, date_revoked,
                         source_id))

            if cur.rowcount != 1:
                raise RepoException("Invalid source relation")
            else:
                return True
