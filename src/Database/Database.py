from os import getenv
from typing import Dict

from psycopg2 import OperationalError
from psycopg2.pool import SimpleConnectionPool


class Database:

    pg_config: Dict = None
    CONNECTION_NAME: str = None

    def __init__(self):
        self.CONNECTION_NAME = getenv('INSTANCE_CONNECTION_NAME')
        self.pg_config = {
          'user': getenv('POSTGRES_USER', '<YOUR DB USER>'),
          'password': getenv('POSTGRES_PASSWORD', '<YOUR DB PASSWORD>'),
          'dbname': getenv('POSTGRES_DATABASE', '<YOUR DB NAME>')
        }

    pg_pool = None

    def __connect(self, host):
        """
        Helper function to connect to Postgres
        """
        self.pg_config['host'] = host
        self.pg_pool = SimpleConnectionPool(1, 1, **self.pg_config)

    def connect(self):
        try:
            self.__connect(f'/cloudsql/{self.CONNECTION_NAME}')
        except OperationalError:
            # If production settings fail, use local development ones
            self.__connect('localhost')

    def get_pool(self):
        if not self.pg_pool:
            self.connect()
        with self.pg_pool.getconn() as conn:
            return conn

    def return_pool(self, pool):
        self.pg_pool.putconn(pool)

    def postgres_demo(self):
        # Initialize the pool lazily, in case SQL access isn't needed for this
        # GCF instance. Doing so minimizes the number of active SQL connections,
        # which helps keep your GCF instances under SQL connection limits.
        if not self.pg_pool:
            self.connect()

        # Remember to close SQL resources declared while running this function.
        # Keep any declared in global scope (e.g. pg_pool) for later reuse.
        with self.pg_pool.getconn() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT NOW() as now')
            results = cursor.fetchone()
            self.pg_pool.putconn(conn)
            return str(results[0])
