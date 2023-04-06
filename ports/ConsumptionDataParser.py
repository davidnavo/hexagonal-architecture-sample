from abc import ABC
from abc import abstractmethod
from typing import Any

from entities.ConsumptionDataType import ConsumptionDataType

class ConsumptionDataParser(ABC):

    @abstractmethod
    def parse(self, row_data:Any) -> ConsumptionDataType: pass

