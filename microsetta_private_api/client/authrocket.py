AUTHROCKET_API_ENDPOINT = 'https://api-e2.authrocket.com/v2/'


def authrocket_api_header(api_key, realm_id):
    """Authenticate a user against authrocket

    Parameters
    ----------
    api_key: str
        An API key from authrocket
    realm_id: str
        A realm ID from authrocket

    Notes
    -----
    Authrocket API access is described in [1]_. In brief, a key must be created
    for a specific realm.

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

    return authrocket_headers
