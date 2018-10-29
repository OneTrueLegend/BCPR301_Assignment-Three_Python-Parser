class SQLError(Exception):
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return "Query Failed: {}".format(self.error_message)