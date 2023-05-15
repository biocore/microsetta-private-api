from enum import Enum
from microsetta_private_api.model.model_base import ModelBase
from microsetta_private_api.model.address import Address


class AuthorizationMatch(Enum):
    FULL_MATCH = 0
    LEGACY_MATCH = 1
    AUTH_ONLY_MATCH = 2
    NO_MATCH = 3


class Account(ModelBase):
    @staticmethod
    def from_dict(input_dict, auth_iss, auth_sub):
        result = Account(
            input_dict["id"],
            input_dict['email'],
            # NOTICE: input_dict is passed by users,
            # we obviously cannot let them declare themselves to be admins :D
            "standard",
            auth_iss,
            auth_sub,
            input_dict['first_name'],
            input_dict['last_name'],
            Address(
                input_dict['address']['street'],
                input_dict['address']['city'],
                input_dict['address']['state'],
                input_dict['address']['post_code'],
                input_dict['address']['country_code']
            ),
            input_dict['latitude'],
            input_dict['longitude'],
            input_dict['cannot_geocode'],
            input_dict['kit_name'],
            input_dict['language'],
        )
        return result

    def __init__(self, account_id, email,
                 account_type, auth_issuer, auth_sub,
                 first_name, last_name,
                 address, latitude, longitude, cannot_geocode,
                 created_with_kit_id, language,
                 creation_time=None, update_time=None):
        self.id = account_id
        self.email = email
        self.account_type = account_type
        self.auth_issuer = auth_issuer
        self.auth_sub = auth_sub
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.cannot_geocode = cannot_geocode
        self.created_with_kit_id = created_with_kit_id
        self.creation_time = creation_time
        self.update_time = update_time
        self.language = language

    def to_api(self):
        # api is not given the auth_issuer or auth_sub
        return {
            "account_id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "address": self.address.to_api(),
            "latitude": self.latitude,
            "longitude": self.longitude,
            "cannot_geocode": self.cannot_geocode,
            "account_type": self.account_type,
            "language": self.language,
            "creation_time": self.creation_time,
            "update_time": self.update_time,
            "kit_name": self.created_with_kit_id
        }

    def account_matches_auth(self, email, auth_issuer, auth_sub):
        # Return values:
        # AuthorizationMatch.FULL_MATCH: email, auth_issuer, and auth_sub on
        # account all match inputs
        # AuthorizationMatch.LEGACY_MATCH: email in account and input match,
        # but BOTH auth_sub and auth_iss in account are None
        # AuthorizationMatch.AUTH_ONLY_MATCH: auth_issuer and auth_sub on
        # account are both non-null and both match those in input, but email in
        # account mismatches input
        # AuthorizationMatch.NO_MATCH: Any other situation, such as none of
        # email, auth_issuer, and auth_sub on account match input; or email in
        # account and input match, but auth_sub and auth_iss on account are
        # both non-null and one or both of them mismatches input; or any weird
        # inconsistent case such as one but not both of auth_issuer and
        # auth_sub on account being null.

        # check if emails match
        email_matches = self.email == email

        auth_info_null = (self.auth_issuer is None and
                          self.auth_sub is None)

        # check auth_iss and auth_sub for account (and require non-nulls)
        auth_info_matches = (not auth_info_null and
                             self.auth_issuer == auth_issuer and
                             self.auth_sub == auth_sub)

        if auth_info_matches and email_matches:
            # everything matches: happy path!
            return AuthorizationMatch.FULL_MATCH

        if auth_info_null and email_matches:
            # legacy account--emails match but has no auth info
            return AuthorizationMatch.LEGACY_MATCH

        if auth_info_matches and not email_matches:
            # maybe this account has no email associated with it in our db,
            # or maybe the user changed their email with the auth provider
            # but DIDN'T change it with us.
            return AuthorizationMatch.AUTH_ONLY_MATCH

        return AuthorizationMatch.NO_MATCH
