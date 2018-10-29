from src.Database.DatabaseResult import DatabaseResult


class SQLiteDatabaseResult(DatabaseResult):

    def size(self):
        return len(self.query)

    def fetch(self):
        return self.query

    def __init__(self, database, query):
        super().__init__(database, query)
