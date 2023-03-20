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

                # staging has site_sampled with "Please select..."
                # and some examples of null source IDs. This is weird, so
                # ignore for now.
                cur.execute("""SELECT ag_kit_barcodes.barcode
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
                               WHERE sample_status='sample-is-valid'
                                   AND site_sampled IS NOT NULL
                                   AND site_sampled != 'Please select...'
                                   AND source_id IS NOT NULL""")

                barcodes = {r[0] for r in cur.fetchall()}
        else:
            barcodes = set(barcodes)

        # determine what samples are already known in qiita
        samples_in_qiita = set(qclient.get('/api/v1/study/10317/samples'))

        # throw away the 10317. study prefix
        samples_in_qiita = {i.split('.', 1)[1] for i in samples_in_qiita}

        # gather the categories currently used in qiita. we no longer need to
        # have parity with Qiita, but we don't want to pass a "missing value"
        # code for any field in Qiita that we aren't passing a real value for
        cats_in_qiita = qclient.get('/api/v1/study/10317/samples/info')
        cats_in_qiita = set(cats_in_qiita['categories'])

        # we will only push samples that are not already present.
        # in testing on stating with qiita-rc, it was observed that
        # large request bodies failed, so we will artificially limit to
        # 1000 samples max per request. We can always use multiple
        # calls to this function if and as needed.
        to_push = list(barcodes - samples_in_qiita)[:1000]

        # short circuit if we do not have anything to push
        if len(to_push) == 0:
            return 0, []

        formatted, error = retrieve_metadata(to_push)
        if len(formatted) == 0:
            return 0, error

        columns = set(formatted.columns)

        # if there are any categories not represented, remark them as
        # missing in the metadata
        for c in cats_in_qiita - columns:
            formatted[c] = MISSING_VALUE

        for_qiita = formatted.to_json(orient='index')
        qclient.http_patch('/api/v1/study/10317/samples', data=for_qiita)
        n_pushed = len(formatted)

        return n_pushed, error
