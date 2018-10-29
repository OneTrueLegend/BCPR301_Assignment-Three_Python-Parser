from abc import ABCMeta, abstractmethod


class DatabaseResult(metaclass=ABCMeta):

    def __init__(self, database, query):
        self.database = database
        self.query = query

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def fetch(self):
        pass
