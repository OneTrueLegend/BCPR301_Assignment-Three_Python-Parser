from abc import ABCMeta, abstractmethod


class DatabaseFactory(metaclass=ABCMeta):
    def __init__(self, db_name):
        self.db_name = db_name

    @abstractmethod
    def query(self, sql):
        pass

    @abstractmethod
    def close(self):
        pass
