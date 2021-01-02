""" Database Settings """
import os
import logging
from masoniteorm.connections import ConnectionResolver


"""
|--------------------------------------------------------------------------
| Load Environment Variables
|--------------------------------------------------------------------------
|
| Loads in the environment variables when this page is imported.
|
"""


"""
The connections here don't determine the database but determine the "connection".
They can be named whatever you want.
"""

DATABASES = {
    'default': 'postgres',
    'mysql': {
        'driver': 'mysql',
        'host': os.getenv('MYSQL_DATABASE_HOST'),
        'user': os.getenv('MYSQL_DATABASE_USER'),
        'password': os.getenv('MYSQL_DATABASE_PASSWORD'),
        'database': os.getenv('MYSQL_DATABASE_DATABASE'),
        'port': os.getenv('MYSQL_DATABASE_PORT'),
        'prefix': '',
        'options': {
            'charset': 'utf8mb4',
        },
        'log_queries': True
    },
    'postgres': {
        'driver': 'postgres',
        'host': 'localhost',
        'user': 'samuel',
        'password': 'samuel',
        'database': 'pingcrm_masonite',
        'port': 5432,
        'prefix': '',
        'log_queries': True
    },
    'sqlite': {
        'driver': 'sqlite',
        'database': 'orm.sqlite3',
        'prefix': '',
        'log_queries': True
    },
    'mssql': {
        'driver': 'mssql',
        'host': os.getenv('MSSQL_DATABASE_HOST'),
        'user': os.getenv('MSSQL_DATABASE_USER'),
        'password': os.getenv('MSSQL_DATABASE_PASSWORD'),
        'database': os.getenv('MSSQL_DATABASE_DATABASE'),
        'port': os.getenv('MSSQL_DATABASE_PORT'),
        'prefix': '',
        'log_queries': True
    },
}

db = ConnectionResolver().set_connection_details(DATABASES)


logger = logging.getLogger('masoniteorm.connection.queries')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()

logger.addHandler(handler)
