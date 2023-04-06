from abc import ABC
from abc import abstractmethod
from typing import Any

class Logger(ABC):
    @abstractmethod
    def log(self, content: Any) -> None: pass
