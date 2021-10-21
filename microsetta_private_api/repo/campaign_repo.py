import psycopg2

from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.campaign import Campaign


class CampaignRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    @staticmethod
    def _row_to_campaign(self, r):
        associated_projects = ", ".join(self._get_projects(r['campaign_id']))
        return Campaign(r['campaign_id'], r['title'], r['instructions'],
                        r['header_image'], r['permitted_countries'],
                        r['language_key'], r['accepting_participants'],
                        associated_projects, r['language_key_alt'],
                        r['title_alt'], r['instructions_alt'])

    @staticmethod
    def _campaign_to_row(c):
        return (c.campaign_id, c.title, c.instructions, c.header_image,
                c.permitted_countries, c.language_key,
                c.accepting_participants, '',
                c.language_key_alt, c.title_alt, c.instructions_alt)

    def _get_projects(self, campaign_id):
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT barcodes.project.project "
                "FROM barcodes.campaigns "
                "LEFT JOIN barcodes.campaigns_projects "
                "ON "
                "barcodes.campaigns.campaign_id = "
                "barcodes.campaigns_projects.campaign_id "
                "LEFT JOIN barcodes.project "
                "ON "
                "barcodes.campaigns_projects.project_id = "
                "barcodes.project.project_id "
                "WHERE "
                "barcodes.campaigns.campaign_id = %s",
                (campaign_id,)
            )

            project_rows = cur.fetchall()
            campaign_projects = [project[0] for project in project_rows]
            return campaign_projects

    def get_all_campaigns(self):
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT campaign_id, title, instructions, header_image, "
                "permitted_countries, language_key, accepting_participants, "
                "language_key_alt, title_alt, "
                "instructions_alt "
                "FROM barcodes.campaigns ORDER BY title"
            )
            rows = cur.fetchall()
            return [self._row_to_campaign(self, r) for r in rows]

    def create_campaign(self, body):
        with self._transaction.cursor() as cur:
            cur.execute(
                "INSERT INTO barcodes.campaigns (title, instructions, "
                "permitted_countries, language_key, accepting_participants, "
                "language_key_alt, title_alt, "
                "instructions_alt) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) "
                "RETURNING campaign_id",
                (body['title'], body['instructions'],
                 body['permitted_countries'], body['language_key'],
                 body['accepting_participants'],
                 body['language_key_alt'], body['title_alt'],
                 body['instructions_alt'])
            )
            campaign_id = cur.fetchone()[0]

            if campaign_id is None:
                raise Exception("Error inserting campaign into database")
            else:
                projects = body['associated_projects'].split(",")
                for project_id in projects:
                    cur.execute(
                        "INSERT INTO barcodes.campaigns_projects ("
                        "campaign_id,project_id"
                        ") VALUES (%s, %s) ",
                        (campaign_id, project_id)
                    )

                self.update_header_image(campaign_id, body['extension'])
                return self.get_campaign_by_id(campaign_id)

    def update_campaign(self, body):
        with self._transaction.cursor() as cur:
            cur.execute(
                "UPDATE barcodes.campaigns SET title = %s, instructions = %s, "
                "permitted_countries = %s, language_key = %s, "
                "accepting_participants = %s, language_key_alt = %s, "
                "title_alt = %s, instructions_alt = %s "
                "WHERE campaign_id = %s",
                (body['title'], body['instructions'],
                 body['permitted_countries'], body['language_key'],
                 body['accepting_participants'], body['language_key_alt'],
                 body['title_alt'], body['instructions_alt'],
                 body['campaign_id'])
            )

            self.update_header_image(body['campaign_id'], body['extension'])

        return self.get_campaign_by_id(body['campaign_id'])

    def get_campaign_by_id(self, campaign_id):
        with self._transaction.dict_cursor() as cur:
            try:
                cur.execute(
                    "SELECT campaign_id, title, instructions, header_image, "
                    "permitted_countries, language_key, "
                    "accepting_participants, "
                    "language_key_alt, title_alt, instructions_alt "
                    "FROM barcodes.campaigns WHERE campaign_id = %s",
                    (campaign_id,)
                )
                r = cur.fetchone()
                if r is None:
                    return None
                else:
                    return self._row_to_campaign(self, r)
            except psycopg2.errors.InvalidTextRepresentation:
                # if someone tries to input a random/malformed campaign ID
                # we just want to return None and let the signup form display
                # the default campaign info
                return None

    def update_header_image(self, campaign_id, extension):
        if len(extension) > 0:
            with self._transaction.cursor() as cur:
                header_image = campaign_id + "." + extension
                cur.execute(
                    "UPDATE barcodes.campaigns SET header_image = %s "
                    "WHERE campaign_id = %s",
                    (header_image, campaign_id)
                )

        return True
