import base64
from microsetta_private_api.config_manager import SERVER_CONFIG


def build_login_redirect(redirect_uri):
    # If a user is externally directed to perform some action, (via email for
    #  example) or is mid action when forced to login, it may be pleasant to
    #  redirect them to a particular page upon successful login.  This is
    #  possible by passing a urlsafe_base64decode'd parameter into the
    #  authrocket login route, which will cause the user to login, register
    #  their token within their active session with our system (and discard the
    #  token so it will not be sent to redirects), then redirect the user to a
    #  to a specified url

    # Because these redirects are GETs they should not be used to perform
    #  actions directly.

    # Example: Redirect to "hello"
    # "aGVsbG8=" == base64.urlsafe_base64encode("hello".encode()).decode()
    # "{{authrocket_url}}/login?redirect_uri={{endpoint}}/authrocket_callback%3Fredirect_uri%3DaGVsbG8=" # noqa

    # Example: Redirect to "https://google.com"
    # "aHR0cHM6Ly9nb29nbGUuY29t" ==
    # base64.urlsafe_base64encode("https://google.com".encode()).decode()
    # "{{authrocket_url}}/login?redirect_uri={{endpoint}}/authrocket_callback%3Fredirect_uri%3DaHR0cHM6Ly9nb29nbGUuY29t" # noqa

    endpoint = SERVER_CONFIG["endpoint"]
    authrocket_url = SERVER_CONFIG["authrocket_url"]
    inside_url = base64.urlsafe_b64encode(redirect_uri.encode()).decode()

    return authrocket_url + \
        "/login?redirect_uri=" + endpoint + \
        "/authrocket_callback%3Fredirect_uri%3D" + inside_url


if __name__ == "__main__":
    print("Build Login Redirect!")
    url = input("Desired URL: ")
    print(build_login_redirect(url))
