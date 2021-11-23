import psycopg2

from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.interested_user import InterestedUser
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
        phone = kwargs['phone']
        address_1 = kwargs['address_1']
        city = kwargs['city']
        state = kwargs['state']
        postal_code = kwargs['postal']
        country = kwargs['country']

        # optional parameters for an interested user:
        acquisition_source = kwargs.get('acquisition_source')
        address_2 = kwargs.get('address_2')
        latitude = kwargs.get('latitude')
        longitude = kwargs.get('longitude')
        confirm_consent = kwargs.get('confirm_consent', False)
        ip_address = kwargs.get('ip_address')
        address_checked = kwargs.get('address_checked', False)
        address_valid = kwargs.get('address_valid', False)

        with self._transaction.cursor() as cur:
            cur.execute(
                "INSERT INTO barcodes.interested_users ("
                "campaign_id, acquisition_source, first_name, last_name, "
                "email, phone, address_1, address_2, city, state, "
                "postal_code, country, latitude, longitude, confirm_consent, "
                "ip_address, address_checked, address_valid, "
                "creation_timestamp) "
                "VALUES ("
                "%s, %s, %s, %s, "
                "%s, %s, %s, %s, %s, %s, "
                "%s, %s, %s, %s, %s, "
                "%s, %s, %s, "
                "NOW()) RETURNING interested_user_id",
                (campaign_id, acquisition_source, first_name, last_name,
                 email, phone, address_1, address_2, city, state,
                 postal_code, country, latitude, longitude, confirm_consent,
                 ip_address, address_checked, address_valid)
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
                "FROM barcodes.interested_users WHERE interested_user_id = %s",
                (interested_user_id,)
            )
            r = cur.fetchone()
            if r is None:
                return None
            else:
                melissa_response = verify_address(r['address_1'],
                                                  r['address_2'],
                                                  r['city'],
                                                  r['state'],
                                                  r['postal_code'],
                                                  r['country'])
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
