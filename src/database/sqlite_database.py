import sqlite3

from src.database.sqlite_error import SQLError
from src.database.sqlite_result import DatabaseResult


class Database:
    """
    Database object containing attribute and functions
    Author: Jake

    >>> db = database("DocTest")
    >>> db.db_name
    'DocTest'
    >>> db.query('CREATE TABLE IF NOT EXISTS TestTable (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT)').fetch()
    []
    >>> db.query("INSERT INTO TestTable VALUES(NULL,'TestName')").fetch()
    []
    >>> db.query('SELECT data FROM TestTable WHERE id=1').fetch()[0]['data']
    'TestName'
    >>> db.query('SELECT data FROM TestTable WHERE id=1').size()
    1
    """

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect("../tmp/" + db_name + '.db')

    # Written By Jake Reddock
    def query(self, sql):
        try:
            self.conn.row_factory = dict_factory
            c = self.conn.cursor()
            c.execute("""PRAGMA encoding="UTF-8";""")
            query_resource = c.execute(sql).fetchall()
            self.conn.commit()
            return DatabaseResult(self, query_resource)
        except sqlite3.OperationalError as err:
            raise SQLError(err)
            # except:
            #     print("Query Failed: An unexpected exception")

    # Written by Jake Reddock
    def close(self):
        """
        Close the connection to the database
        """
        self.conn.close()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
