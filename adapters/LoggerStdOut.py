from typing import Any
from ports.Logger import Logger

class LoggerStdOut(Logger):
    def log(self, content: Any) -> None:
        print(repr(content))