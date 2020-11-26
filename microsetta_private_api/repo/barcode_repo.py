from microsetta_private_api.model.preparation import Preparation
from microsetta_private_api.repo.base_repo import BaseRepo


class BarcodeRepo(BaseRepo):
    """
    Repo handling interactions with barcodes.barcode and surrounding tables
    """

    @staticmethod
    def _row_to_prep(r):
        return Preparation(
            barcode=r["barcode"],
            preparation_id=r["preparation_id"],
            preparation_type=r["preparation_type"],
            num_sequences=r["num_sequences"]
        )

    @staticmethod
    def _prep_to_row(p):
        return (p.barcode,
                p.preparation_id,
                p.preparation_type,
                p.num_sequences)

    def list_preparations(self, barcode):
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT "
                "barcode, preparation_id, preparation_type, num_sequences "
                "FROM preparation "
                "WHERE barcode=%s", (barcode,)
            )
            rows = cur.fetchall()
            return [self._row_to_prep(r) for r in rows]

    def delete_preparation(self, barcode, preparation_id):
        with self._transaction.cursor() as cur:
            cur.execute(
                "DELETE FROM preparation "
                "WHERE barcode=%s AND preparation_id=%s",
                (barcode, preparation_id,)
            )
            return cur.rowcount == 1

    def upsert_preparation(self, preparation: Preparation):
        self.delete_preparation(preparation.barcode,
                                preparation.preparation_id)
        with self._transaction.cursor() as cur:
            cur.execute(
                "INSERT into preparation"
                "(barcode, preparation_id, preparation_type, num_sequences)"
                "VALUES(%s, %s, %s, %s)", self._prep_to_row(preparation)
            )
