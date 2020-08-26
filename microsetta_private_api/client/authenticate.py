import requests


AUTHROCKET_API_ENDPOINT = 'https://api-e2.authrocket.com/v2/'


class AuthenticationError(Exception):
    pass


class UserNotFound(Exception):
    pass


class UserPasswordInvalid(Exception):
    pass


def authrocket(api_key, realm_id, email, password):
    """Authenticate a user against authrocket

    Parameters
    ----------
    api_key: str
        An API key from authrocket
    realm_id: str
        A realm ID from authrocket
    email: str
        The user to attempt to login as
    password: str
        The password for the user

    Notes
    -----
    Authrocket API access is described in [1]_. In brief, a key must be created
    for a specific realm. In order to authenticate a user, the key must have
    read and write permissions.

    Raises
    ------
    AuthenticationError
        If the Authrocket key, realm or permissions on the key were not
        accepted
    UserNotFound
        If the Authrocket authentication worked, but the requested user
        was not found.
    UserPasswordInvalid
        If the user password was invalid.
    Exception
        If an unrecognized status code is returned.

    Returns
    -------
    dict
        Headers appropriate for microsetta-private-api interaction

    References
    ----------
    .. [1] https://authrocket.com/docs/api
    """
    # https://authrocket.com/docs/api/accessing_authrocket#request-headers
    authrocket_headers = {'Authorization': f'Bearer {api_key},{realm_id}',
                          'Content-Type': 'application/json'}

    # https://authrocket.com/docs/api/users#method-authenticate
    authenticate_url = f'{AUTHROCKET_API_ENDPOINT}/users/{email}/authenticate'

    authrocket_response = requests.post(authenticate_url,
                                        headers=authrocket_headers)

    # https://authrocket.com/docs/api/status_codes
    if authrocket_response.status_code == 403:
        raise AuthenticationError()
    elif authrocket_response.status_code == 404:
        raise UserNotFound()
    elif authrocket_response.status_code == 422:
        raise UserPasswordInvalid()
    elif authrocket_response.status_code != 201:
        raise Exception("Unrecognized status code: %d" %
                        authrocket_response.status_code)

    authrocket_token = authrocket_response.json()['token']

    return {'Authorization': f'Bearer {authrocket_token}'}
