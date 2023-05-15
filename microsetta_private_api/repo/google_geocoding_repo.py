from microsetta_private_api.repo.base_repo import BaseRepo


class GoogleGeocodingRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def create_record(self, request_address):
        """
        Create a record before pinging Google so we have visibility into
        failed requests

        Parameters
        ----------
        request_address : str
            Formatted address to geocode

        Returns
        -------
        geocoding_request_id : uuid4
            Unique ID of the record in the ag.google_geocoding table
        """
        with self._transaction.cursor() as cur:
            cur.execute("""INSERT INTO ag.google_geocoding (request_address)
                           VALUES (%s)
                           RETURNING geocoding_request_id""",
                        (request_address, ))
            geocoding_request_id = cur.fetchone()[0]

            if geocoding_request_id is None:
                return None
            else:
                return geocoding_request_id

    def get_record(self, geocoding_request_id):
        """
        Create a record before pinging Google so we have visibility into
        failed requests

        Parameters
        ----------
        geocoding_request_id : uuid4
            Unique ID of the record in the ag.google_geocoding table

        Returns
        -------
        None or response_body : json
            None if no record is found
            The json object with geocoding data if record exists
        """
        with self._transaction.dict_cursor() as cur:
            cur.execute("""SELECT response_body
                           FROM ag.google_geocoding
                           WHERE geocoding_request_id = %s""",
                        (geocoding_request_id, ))
            row = cur.fetchone()
            if row is None:
                return None
            else:
                return row['response_body']

    def update_record(self, geocoding_request_id, response_body):
        """
        Update the DB record with the geocoding response
        Parameters
        ----------
        geocoding_request_id : uuid4
            Unique ID of the record in the ag.google_geocoding table
        response_body : json
            The response from Google's Geocoding API

        Returns
        -------
        bool
            Whether the number of updated rows == 1
        """
        with self._transaction.dict_cursor() as cur:
            cur.execute("""UPDATE ag.google_geocoding
                           SET response_body = %s
                           WHERE geocoding_request_id = %s""",
                        (response_body, geocoding_request_id))
            return cur.rowcount == 1

    def check_duplicate(self, request_address):
        """
        Check if we already have geocoding data for a given address

        Parameters
        ----------
        request_address : str
            Formatted address to geocode

        Returns
        -------
        None or geocoding_request_id : uuid4
            None if no record exists
            The geocoding_request_id if one does exist
        """
        with self._transaction.dict_cursor() as cur:
            cur.execute("""SELECT geocoding_request_id
                           FROM ag.google_geocoding
                           WHERE request_address = %s""",
                        (request_address, ))
            row = cur.fetchone()
            if row is None:
                return None
            else:
                return row['geocoding_request_id']
