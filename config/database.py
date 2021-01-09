""" Database Settings """
import os
import logging
from masonite.environment import LoadEnvironment, env
from masoniteorm.connections import ConnectionResolver

"""
|--------------------------------------------------------------------------
| Load Environment Variables
|--------------------------------------------------------------------------
|
| Loads in the environment variables when this page is imported.
|
"""

LoadEnvironment()

"""
The connections here don't determine the database but determine the "connection".
They can be named whatever you want.
"""

DATABASES = {
    "default": "postgres",
    "mysql": {
        "driver": "mysql",
        "host": env("MYSQL_DATABASE_HOST"),
        "user": env("MYSQL_DATABASE_USER"),
        "password": env("MYSQL_DATABASE_PASSWORD"),
        "database": env("MYSQL_DATABASE_DATABASE"),
        "port": env("MYSQL_DATABASE_PORT"),
        "prefix": "",
        "grammar": "mysql",
        "options": {
            "charset": "utf8mb4",
        },
        "log_queries": True,
    },
    "postgres": {
        "driver": "postgres",
        "host": env("DB_HOST"),
        "user": env("DB_USERNAME"),
        "password": env("DB_PASSWORD"),
        "database": env("DB_DATABASE"),
        "port": env("DB_PORT"),
        "prefix": "",
        "log_queries": True,
    },
    "sqlite": {
        "driver": "sqlite",
        "database": "orm.sqlite3",
        "prefix": "",
        "log_queries": True,
    },
    "mssql": {
        "driver": "mssql",
        "host": env("MSSQL_DATABASE_HOST"),
        "user": env("MSSQL_DATABASE_USER"),
        "password": env("MSSQL_DATABASE_PASSWORD"),
        "database": env("MSSQL_DATABASE_DATABASE"),
        "port": env("MSSQL_DATABASE_PORT"),
        "prefix": "",
        "log_queries": True,
    },
}

DB = ConnectionResolver().set_connection_details(DATABASES)


logger = logging.getLogger("masoniteorm.connection.queries")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()

logger.addHandler(handler)
