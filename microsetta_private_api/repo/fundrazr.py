import psycopg2


class DuplicateTransaction(psycopg2.UniqueViolation):
    pass


class UnknownItem():
    pass



