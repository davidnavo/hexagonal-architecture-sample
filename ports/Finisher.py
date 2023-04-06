from abc import ABC
from abc import abstractmethod

class Finisher(ABC):
    @abstractmethod
    def end(self) -> None: pass
