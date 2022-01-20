from microsetta_private_api.config_manager import AMGUT_CONFIG
import psycopg2.pool
import psycopg2.extras
import atexit
from psycopg2 import sql


class Transaction:
    # Note: SimpleConnectionPool works only for single threaded applications
    #  Should we make the server multi threaded, we must switch to a
    #  ThreadedConnectionPool
    _POOL = psycopg2.pool.SimpleConnectionPool(
        1,
        20,
        user=AMGUT_CONFIG.user,
        password=AMGUT_CONFIG.password,
        database=AMGUT_CONFIG.database,
        host=AMGUT_CONFIG.host,
        port=AMGUT_CONFIG.port)

    @staticmethod
    @atexit.register
    def shutdown_pool():
        Transaction._POOL.closeall()

    def __init__(self):
        self._closed = True
        self._conn = None

    def __enter__(self):
        self._closed = False
        self._conn = Transaction._POOL.getconn()
        return self

    def __exit__(self, type, value, traceback):
        if not self._closed:
            self.rollback()
        Transaction._POOL.putconn(self._conn)

    def lock_table(self, table):
        # Just access exclusive mode for now- hard to escape the lock mode
        # in psycopg2.
        with self.cursor() as cur:
            cur.execute(
                sql.SQL("LOCK TABLE {} IN ACCESS EXCLUSIVE MODE")
                .format(sql.Identifier(table))
            )

    def commit(self):
        if self._closed:
            raise RuntimeError("Cannot commit closed Transaction")
        self._conn.commit()
        self._closed = True

    def rollback(self):
        if self._closed:
            raise RuntimeError("Cannot rollback closed Transaction")
        self._conn.rollback()
        self._closed = True

    def cursor(self):
        if self._closed:
            raise RuntimeError("Cannot open cursor from closed Transaction")
        cur = self._conn.cursor()
        cur.execute('SET search_path TO ag, barcodes, public')
        return cur

    def dict_cursor(self):
        if self._closed:
            raise RuntimeError("Cannot open cursor from closed Transaction")
        cur = self._conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('SET search_path TO ag, barcodes, public')
        return cur

    @property
    def conn(self):
        return self._conn
