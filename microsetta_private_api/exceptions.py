# Note: werkzeug has error handlers for most http codes, but it doesn't have
# 422.  Are we sure this is a standard error code?  Anyway, we need a custom
# exception to register for 422 and RepoException will work for it.


class RepoException(Exception):
    """
    Converts psycopg2 exceptions into messages
    that can be displayed to the user
    """
    pass
