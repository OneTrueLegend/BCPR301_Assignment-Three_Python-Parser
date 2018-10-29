import sqlite3

from src.Database.DatabaseFactory import DatabaseFactory
from src.Database.SQLiteDatabaseResult import SQLiteDatabaseResult


class SQLiteDatabaseFactory(DatabaseFactory):

    def query(self, sql):
        try:
            self.conn.row_factory = dict_factory
            c = self.conn.cursor()
            c.execute("""PRAGMA encoding="UTF-8";""")
            query_resource = c.execute(sql).fetchall()
            self.conn.commit()
            return SQLiteDatabaseResult(self, query_resource)
        except sqlite3.OperationalError as err:
            raise SQLError(err)
            # except:
            #     print("Query Failed: An unexpected exception")

    def close(self):
        """
        Close the connection to the database
        """
        self.conn.close()

    def __init__(self, db_name):
        super().__init__(db_name)
        self.conn = sqlite3.connect("../tmp/" + db_name + '.db')

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d