from uuid import UUID

from psycopg2._json import Json

from microsetta_private_api.model.log_event import LogEvent, EventType, \
    EventSubtype
from microsetta_private_api.repo.base_repo import BaseRepo


_read_cols = "id, event_type, event_subtype, event_time, event_state"


def _event_to_row(event: LogEvent):
    return {
        "id": str(event.event_id),
        "event_type": event.event_type.value,
        "event_subtype": event.event_subtype.value,
        # event_time is set by db upon creation, need not be passed in.
        "event_state": Json(event.event_state),
    }


def _row_to_event(row):
    return LogEvent(UUID(row['id']),
                    EventType(row['event_type']),
                    EventSubtype(row['event_subtype']),
                    row['event_time'],
                    row['event_state'])


class EventLogRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def add_event(self, event: LogEvent):
        with self._transaction.cursor() as cur:
            cur.execute("INSERT INTO event_log("
                        "id, "
                        "event_type, "
                        "event_subtype, "
                        "event_state"
                        ") VALUES ("
                        "%(id)s, "
                        "%(event_type)s, "
                        "%(event_subtype)s, "
                        "%(event_state)s"
                        ")",
                        _event_to_row(event))
            return cur.rowcount == 1

    def get_events(self):
        with self._transaction.dict_cursor() as cur:
            cur.execute("SELECT " + _read_cols + " FROM "
                        "event_log "
                        "ORDER BY "
                        "event_time DESC")
            return [_row_to_event(row) for row in cur.fetchall()]

    def get_events_by_type(self, event_type: EventType):
        with self._transaction.dict_cursor() as cur:
            cur.execute("SELECT " + _read_cols + " FROM "
                        "event_log "
                        "WHERE "
                        "event_type = %s "
                        "ORDER BY "
                        "event_time DESC",
                        (event_type.value,))
            return [_row_to_event(row) for row in cur.fetchall()]

    def get_events_by_subtype(self,
                              event_type: EventType,
                              event_subtype: EventSubtype):
        with self._transaction.dict_cursor() as cur:
            cur.execute("SELECT " + _read_cols + " FROM "
                        "event_log "
                        "WHERE "
                        "event_type = %s AND "
                        "event_subtype = %s "
                        "ORDER BY "
                        "event_time DESC",
                        (event_type.value, event_subtype.value))
            return [_row_to_event(row) for row in cur.fetchall()]

    # See https://www.postgresql.org/docs/9.5/functions-json.html#FUNCTIONS-JSON-OP-TABLE  # noqa
    # to understand referencing email field from jsonb representation

    # TODO: I believe the LIKE operator can make use of the btree index i've
    #  set on this table so long as the pattern specified is a case sensitive
    #  prefix.  To support ILIKE or searching middle of email field, may have
    #  to pull it out of the jsonb field, or dive into gin_trgm_ops
    #  See https://stackoverflow.com/questions/33025890/indexing-jsonb-data-for-pattern-matching-searches # noqa
    def get_events_by_email(self, email: str):
        with self._transaction.dict_cursor() as cur:
            cur.execute("SELECT " + _read_cols + " FROM "
                        "event_log "
                        "WHERE "
                        "event_state->>'email' LIKE %s "
                        "ORDER BY "
                        "event_state->>'email', event_time DESC",
                        # Do not change this pattern without analyzing
                        # the query in postgres to ensure it uses indexes
                        (email+"%",))
            return [_row_to_event(row) for row in cur.fetchall()]

    def get_events_by_account(self, account_id: UUID):
        with self._transaction.dict_cursor() as cur:
            cur.execute("SELECT " + _read_cols + " FROM "
                        "event_log "
                        "WHERE "
                        "event_state->>'account_id' = %s "
                        "ORDER BY "
                        "event_time DESC",
                        (str(account_id),))
            return [_row_to_event(row) for row in cur.fetchall()]

    def delete_event(self, event_id: UUID):
        with self._transaction.cursor() as cur:
            cur.execute("DELETE FROM event_log "
                        "WHERE "
                        "id = %s",
                        (str(event_id),))
            return cur.rowcount == 1
