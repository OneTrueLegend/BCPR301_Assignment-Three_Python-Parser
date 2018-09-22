class DatabaseResult:
    """
    Database Result object containing attributes and functions
    Author: Jake

    >>> database = database("DocTest")
    >>> query = database.conn.cursor().execute('SELECT data FROM TestTable WHERE id=1').fetchall()
    >>> database_result(database, query).size()
    1
    >>> query = database.conn.cursor().execute('SELECT data FROM TestTable WHERE id=1').fetchall()
    >>> database_result(database, query).fetch()[0][0]
    'TestName'
    """
    def __init__(self, database, query):
        self.database = database
        self.query = query

    # Written By Jake Reddock
    def size(self):
        return len(self.query)

    # Written By Jake Reddock
    def fetch(self):
        return self.query


