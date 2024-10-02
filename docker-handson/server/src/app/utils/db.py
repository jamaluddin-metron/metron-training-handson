import sqlite3
from .logger import get_logger
from .constants import Constants

logger = get_logger(__name__)

# Define class to establish connection to DB, and perform CRUD Operations
# on Data Model.

class Database:
    def __init__(self):
        self.db_name = Constants.DB_NAME + ".db"

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self, create_table_sql) -> bool:
        transaction_status = False
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute(create_table_sql)
            conn.commit()
            transaction_status = True
        except sqlite3.Error as e:
            logger.error(f"Error Occured while trying to store logs in DB:\n{e}")
        finally:
            conn.close()
            return transaction_status

    def insert(self, table, columns, values):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO {table} ({columns}) VALUES ({values})")
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

    def select(self, table, columns="*", where_clause=""):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            query = f"SELECT {columns} FROM {table} {where_clause}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

    def update(self, table, set_clause, where_clause):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
            cursor.execute(query)
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

    def delete(self, table, where_clause):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            query = f"DELETE FROM {table} WHERE {where_clause}"
            cursor.execute(query)
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()