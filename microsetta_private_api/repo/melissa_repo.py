from microsetta_private_api.repo.base_repo import BaseRepo


class MelissaRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def create_record(self, address_1, address_2, city, state, postal,
                      country):
        """
        Create a record before pinging Melissa so we can include unique ID

        Parameters
        ----------
        address_1 - Primary street address (e.g. 123 Main St)
        address_2 - Secondary street address (e.g. Apt 555)
        city - City (e.g. San Diego)
        state - State (e.g. CA)
        postal - Postal code (e.g. 92116)
        country - Country (e.g. United States)

        Returns
        -------
        record_id - Unique ID of the address verification record
        """
        with self._transaction.cursor() as cur:
            cur.execute("""INSERT INTO campaign.melissa_address_queries (
                            query_timestamp,
                            source_address_1,
                            source_address_2,
                            source_city,
                            source_state,
                            source_postal,
                            source_country)
                            VALUES (NOW(), %s, %s, %s, %s, %s, %s)
                            RETURNING melissa_address_query_id""",
                        (address_1, address_2, city, state, postal, country))
            record_id = cur.fetchone()[0]

            if record_id is None:
                return None
            else:
                return record_id

    def check_duplicate(self, address_1, address_2, postal, country):
        """
        Check if an address has already been verified to avoid duplicate
            queries against the Melissa API

        Note: We ignore city and state because they're superfluous for the
            purpose of deduplication. A street address, postal code,
            and country are sufficient for purposes of unique identification.

        Parameters
        ----------
        address_1 - Primary street address
        address_2 - Secondary street address
        postal - Postal code
        country - Country

        Returns
        -------
        False if record is not a duplicate
        Full table row is record is a duplicate
        """
        with self._transaction.dict_cursor() as cur:
            cur.execute("""SELECT * FROM campaign.melissa_address_queries
                            WHERE (source_address_1 = %s
                            AND source_address_2 = %s
                            AND source_postal = %s
                            AND source_country = %s
                            AND result_processed = true)
                            OR (result_address_1 = %s
                            AND result_address_2 = %s
                            AND result_postal = %s
                            AND result_country = %s
                            AND result_processed = true)""",
                        (address_1, address_2, postal, country,
                         address_1, address_2, postal, country))
            row = cur.fetchone()
            if row is None:
                return False
            else:
                return row

    def update_results(self, record_id, source_url, result_raw,
                       result_codes, result_good, formatted_address,
                       address_1, address_2, city, state, postal, country,
                       latitude, longitude):
        """
        Update record in the database with the results from the Melissa API

        Note: We store the formatted address, as well as the constituent
            elements for ease of use. There may be future cases where using
            the pre-formatted address makes more sense.

        Parameters
        ----------
        record_id - Unique ID generated from create_record function
        source_url - URL we used to query Melissa (for record-keeping/debug)
        result_raw - Full response from Melissa
        result_codes - Codes indicating whether address is valid, why, and
                        what fields were updated
        result_good - Our internal good/bad flag based on result_codes
        formatted_address - The fully formatted address returned from API
        address_1 - First address line returned from API
        address_2 - Second address line returned from API
        city - City returned from API
        state - State returned from API
        postal - Postal returned from API
        country - Country returned from API
        latitude - Latitude returned from API
        longitude - Longitude returned from API

        Returns
        -------
        bool - True if a row was updated

        """

        # if the result doesn't contain lat/long, need to set them to null
        # otherwise, they default to '' and cause a database error on update
        if not latitude:
            latitude = None

        if not longitude:
            longitude = None

        with self._transaction.cursor() as cur:
            cur.execute("""UPDATE campaign.melissa_address_queries SET
                                result_processed = true,
                                source_url = %s,
                                result_raw = %s,
                                result_codes = %s,
                                result_good = %s,
                                result_formatted_address = %s,
                                result_address_1 = %s,
                                result_address_2 = %s,
                                result_city = %s,
                                result_state = %s,
                                result_postal = %s,
                                result_country = %s,
                                result_latitude = %s,
                                result_longitude = %s
                                WHERE melissa_address_query_id = %s""",
                        (source_url, result_raw, result_codes, result_good,
                         formatted_address, address_1, address_2, city, state,
                         postal, country, latitude, longitude, record_id))
            return cur.rowcount == 1
