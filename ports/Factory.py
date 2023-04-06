from abc import ABC
from abc import abstractmethod

class Factory(ABC) :
    @classmethod
    def get(cls) : pass
