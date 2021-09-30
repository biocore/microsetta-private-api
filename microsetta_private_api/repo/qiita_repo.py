from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.qiita import qclient
from microsetta_private_api.repo.metadata_repo import retrieve_metadata
from microsetta_private_api.repo.metadata_repo._constants import MISSING_VALUE


class QiitaRepo(BaseRepo):
    def push_metadata_to_qiita(self, barcodes=None):
        """Attempt to format and push metadata for the set of barcodes

        Only barcodes not currently represented in Qiita will be pushed.

        Parameters
        ----------
        barcodes : Iterable or None
            The list of barcodes to attempt to push. If None, all
            "sample-is-valid", as based on their latest scan, will be
            used.

        Notes
        -----
        We are NOT capturing exceptions from the QiitaClient. These errors
        should all be pathological.

        Raises
        ------
        KeyError
            If metadata categories from Microsetta are observed to NOT
            exist in Qiita.

        Returns
        -------
        int
            The number of successfully pushed samples to Qiita
        list
            Any error detail when constructing metadata
        """
        if barcodes is None:
            with self._transaction.cursor() as cur:
                # obtain all barcodes, which are part of the AG table,
                # which report as their latest scan being valid
                cur.execute("""SELECT CONCAT('10317.', ag_kit_barcodes.barcode)
                               FROM ag.ag_kit_barcodes
                               INNER JOIN barcodes.barcode_scans USING(barcode)
                               INNER JOIN (
                                   SELECT barcode,
                                      max(scan_timestamp)
                                          AS scan_timestamp_latest
                                   FROM barcodes.barcode_scans
                                   GROUP BY barcode
                               ) AS latest_scan
                               ON barcode_scans.barcode = latest_scan.barcode
                                   AND barcode_scans.scan_timestamp =
                                       latest_scan.scan_timestamp_latest
                               WHERE sample_status='sample-is-valid'""")
                barcodes = {r[0] for r in cur.fetchall()}
        else:
            barcodes = set(barcodes)

        # determine what samples are already known in qiita
        samples_in_qiita = set(qclient.get('/api/v1/study/10317/samples'))

        # gather the categories currently used in qiita. we have to have parity
        # with the categories when pushing
        cats_in_qiita = qclient.get('/api/v1/study/10317/samples/info')
        cats_in_qiita = set(cats_in_qiita['categories'])

        # we will only push samples that are not already present
        to_push = list(barcodes - samples_in_qiita)

        # short circuit if we do not have anything to push
        if len(to_push) == 0:
            return 0, []

        formatted, error = retrieve_metadata(to_push)

        columns = set(formatted.columns)

        # the qiita endpoint will not allow for adding new categories
        # and we can determine this before we poke qiita.
        # TODO: allow adding new columns to Qiita
        if not cats_in_qiita.issuperset(columns):
            formatted = formatted[cats_in_qiita & columns]

        # if there are any categories not represented, remark them as
        # missing in the metadata
        for c in cats_in_qiita - columns:
            formatted.columns[c] = MISSING_VALUE

        for_qiita = formatted.to_json(orient='index')
        qclient.http_patch('/api/v1/study/10317/samples', data=for_qiita)

        n_pushed = len(formatted)

        return n_pushed, error
