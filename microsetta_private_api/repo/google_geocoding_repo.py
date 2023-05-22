from microsetta_private_api.repo.base_repo import BaseRepo


class GoogleGeocodingRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def get_or_create_record(self, request_address):
        """
        Check if a record for a given address exists. If it does, return the
        record's response_body. If it does not, create a record and return the
        id

        Parameters
        ----------
        request_address : str
            Formatted address to geocode

        Returns
        -------
        new_record : bool
            Boolean flag indicating whether it's a new record
        geocoding_request_id : uuid4 or response_body : json
            Unique ID of the record in the ag.google_geocoding table OR
            json object with geocoding data
        """
        with self._transaction.dict_cursor() as cur:
            # Lock the table to prevent a race condition
            self._transaction.lock_table("google_geocoding")

            # Check to see if we've geocoded the address before
            cur.execute("""SELECT response_body
                           FROM ag.google_geocoding
                           WHERE request_address = %s""",
                        (request_address, ))
            row = cur.fetchone()
            if row is None:
                # It's a new geocoding request, create a record in the table
                cur.execute("""INSERT INTO ag.google_geocoding (request_address)
                               VALUES (%s)
                               RETURNING geocoding_request_id""",
                            (request_address,))
                geocoding_request_id = cur.fetchone()[0]
                return True, geocoding_request_id
            else:
                # Already geocoded, return the response body
                return False, row['response_body']

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
