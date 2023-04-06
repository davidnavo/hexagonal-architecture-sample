from abc import ABC
from abc import abstractmethod

from entities.ConsumptionDataType import ConsumptionDataType
from ports.ConsumptionDataParser import ConsumptionDataParser

class ConsumptionFileProcessor(ConsumptionDataParser):
    
    @abstractmethod
    def __init__(self, filename: str) -> str: pass
    
    @abstractmethod
    def consumption_data(self) -> list[ConsumptionDataType]: pass