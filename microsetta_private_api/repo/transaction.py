from LEGACY.config_manager import AMGUT_CONFIG
import psycopg2


class Transaction:

    def __init__(self):
        self._closed = True
        self._conn = None

    def __enter__(self):
        self._closed = False
        # Note, we may want to switch to a connection pool in the future
        self._conn = psycopg2.connect(user=AMGUT_CONFIG.user,
                                      password=AMGUT_CONFIG.password,
                                      database=AMGUT_CONFIG.database,
                                      host=AMGUT_CONFIG.host,
                                      port=AMGUT_CONFIG.port)
        return self

    def __exit__(self, type, value, traceback):
        if not self._closed:
            self.rollback()

    def commit(self):
        if self._closed:
            raise RuntimeError("Cannot commit closed Transaction")
        self._conn.commit()
        self._conn.close()
        self._closed = True

    def rollback(self):
        if self._closed:
            raise RuntimeError("Cannot rollback closed Transaction")
        self._conn.rollback()
        self._conn.close()
        self._closed = True

    def cursor(self):
        if self._closed:
            raise RuntimeError("Cannot open cursor from closed Transaction")
        cur = self._conn.cursor()
        cur.execute('SET search_path TO ag, barcodes, public')
        return cur
