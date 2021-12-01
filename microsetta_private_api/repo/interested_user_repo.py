from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.util.melissa import verify_address


class InterestedUserRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def insert_interested_user(self, **kwargs):
        # required parameters for an interested user:
        campaign_id = kwargs['campaign_id']
        first_name = kwargs['first_name']
        last_name = kwargs['last_name']
        email = kwargs['email']

        # optional parameters for an interested user:
        acquisition_source = kwargs.get('acquisition_source')
        phone = kwargs.get('phone')
        address_1 = kwargs.get('address_1')
        address_2 = kwargs.get('address_2')
        city = kwargs.get('city')
        state = kwargs.get('state')
        postal_code = kwargs.get('postal')
        country = kwargs.get('country')
        latitude = kwargs.get('latitude')
        longitude = kwargs.get('longitude')
        confirm_consent = kwargs.get('confirm_consent', False)
        ip_address = kwargs.get('ip_address')
        address_checked = kwargs.get('address_checked', False)
        address_valid = kwargs.get('address_valid', False)
        over_18 = kwargs.get('over_18', False)

        with self._transaction.cursor() as cur:
            cur.execute(
                "INSERT INTO barcodes.interested_users ("
                "campaign_id, acquisition_source, first_name, last_name, "
                "email, phone, address_1, address_2, city, state, "
                "postal_code, country, latitude, longitude, confirm_consent, "
                "ip_address, address_checked, address_valid, over_18, "
                "creation_timestamp) "
                "VALUES ("
                "%s, %s, %s, %s, "
                "%s, %s, %s, %s, %s, %s, "
                "%s, %s, %s, %s, %s, "
                "%s, %s, %s, %s, "
                "NOW()) RETURNING interested_user_id",
                (campaign_id, acquisition_source, first_name, last_name,
                 email, phone, address_1, address_2, city, state,
                 postal_code, country, latitude, longitude, confirm_consent,
                 ip_address, address_checked, address_valid, over_18)
            )
            interested_user_id = cur.fetchone()[0]

            if interested_user_id is None:
                raise RepoException("Error inserting interested user")
            else:
                self.verify_address(interested_user_id)

                return interested_user_id

    def verify_address(self, interested_user_id):
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT address_1, address_2, city, state, postal_code, "
                "country "
                "FROM barcodes.interested_users WHERE interested_user_id = %s "
                "AND address_checked = false AND address_1 != '' AND "
                "postal_code != '' AND country != ''",
                (interested_user_id,)
            )
            r = cur.fetchone()
            if r is None:
                return None
            else:
                try:
                    melissa_response = verify_address(r['address_1'],
                                                      r['address_2'],
                                                      r['city'],
                                                      r['state'],
                                                      r['postal_code'],
                                                      r['country'])
                except Exception as e:
                    raise RepoException(e)

                if melissa_response['valid'] is True:
                    # For valid addresses, we append the latitude/longitude
                    # and silently update the address to the Melissa-verified
                    # version. However, we leave country alone to maintain
                    # consistency with internal country names
                    cur.execute(
                        "UPDATE barcodes.interested_users "
                        "SET address_checked = true, address_valid = true, "
                        "address_1 = %s, address_2 = %s, city = %s, "
                        "state = %s, postal_code = %s, "
                        "latitude = %s, longitude = %s "
                        "WHERE interested_user_id = %s",
                        (melissa_response['address_1'],
                         melissa_response['address_2'],
                         melissa_response['city'],
                         melissa_response['state'],
                         melissa_response['postal'],
                         melissa_response['latitude'],
                         melissa_response['longitude'],
                         interested_user_id,)
                    )
                else:
                    cur.execute(
                        "UPDATE barcodes.interested_users "
                        "SET address_checked = true, address_valid = false "
                        "WHERE interested_user_id = %s",
                        (interested_user_id,)
                    )

                return True
