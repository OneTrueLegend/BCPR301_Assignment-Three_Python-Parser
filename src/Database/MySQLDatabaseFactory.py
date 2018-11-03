import mysql.connector

from src.Database.DatabaseFactory import DatabaseFactory
from src.Database.MySQLDatabaseResult import MySQLDatabaseResult
from src.Database.SQLError import SQLError


class MySQLDatabaseFactory(DatabaseFactory):

    def query(self, sql):
        try:
            c = self.conn.cursor(dictionary=True)
            c.execute(sql)
            if c.description is not None:
                query_resource = c.fetchall()
                return MySQLDatabaseResult(self, query_resource)
            else:
                self.conn.commit()
        except mysql.connector.errors.DatabaseError as err:
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
        self.conn = mysql.connector.connect(host="localhost", user="root")
        self.query("CREATE DATABASE IF NOT EXISTS {}".format(db_name))
        # self.query("USE {}".format(db_name))
        self.conn.database = db_name
