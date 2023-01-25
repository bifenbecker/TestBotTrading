import psycopg2
from constants import *


class PostgresConnection:
    """
    Context manager of connection to database - Postgres
    """

    def __enter__(self):
        self.__conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                            password=DB_PASSWORD, host=DB_HOST, port='5439')

        return self.__conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__conn.close()

