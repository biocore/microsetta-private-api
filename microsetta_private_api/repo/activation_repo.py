from microsetta_private_api.model.activation_code import ActivationCode
from microsetta_private_api.repo.base_repo import BaseRepo


class ActivationRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    @staticmethod
    def to_api(row):
        return {
            "email": row[0],
            "code": row[1],
            "activated": row[2]
        }

    def search_email(self, email_query):
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT email, code, activated FROM "
                "activation WHERE email LIKE %s", (email_query + "%",)
            )
            return [ActivationRepo.to_api(r) for r in cur.fetchall()]

    def search_code(self, code_query):
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT email, code, activated FROM "
                "activation WHERE code LIKE %s", (code_query + "%")
            )
            return [ActivationRepo.to_api(r) for r in cur.fetchall()]

    def get_activation_code(self, email):
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT code "
                "FROM activation "
                "WHERE email=%s", (email,))
            r = cur.fetchone()
            if r is not None:
                # Already an activation code available
                # for this email, return it.
                return r[0]

            code_in_db = True
            while code_in_db:
                code = ActivationCode.generate()
                cur.execute(
                    "SELECT email "
                    "FROM activation "
                    "WHERE code=%s", (code,))
                # Collisions should be EXTREMELY rare.
                code_in_db = cur.fetchone() is not None

            # Now that we have an unused code,
            # write it to db
            cur.execute(
                "INSERT INTO "
                "activation(email, code, activated) "
                "VALUES(%s, %s, %s)",
                (email, code, False)
            )
            return code

    def get_activation_codes(self, emails):
        result = {}
        for email in emails:
            code = self.get_activation_code(email)
            result[email] = code
        return result

    def can_activate(self, email, code):
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT email, code, activated "
                "FROM activation WHERE "
                "email = %s AND "
                "code = %s",
                (email, code)
            )
            row = cur.fetchone()
            # Can activate if that email is associated
            # with that code
            if row is None:
                return False
            # AND the code is not yet activated.
            return row[2] is False

    def use_activation_code(self, email, code):
        if not self.can_activate(email, code):
            return False
        with self._transaction.cursor() as cur:
            cur.execute(
                "UPDATE activation "
                "SET activated=true "
                "WHERE email=%s AND code=%s",
                (email, code)
            )
            return cur.rowcount == 1