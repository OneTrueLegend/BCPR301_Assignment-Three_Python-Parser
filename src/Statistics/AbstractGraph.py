from abc import ABCMeta, abstractmethod


class AbstractGraph(metaclass=ABCMeta):
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def insert(self, points=()):
        pass

    @abstractmethod
    def finalize(self):
        pass
