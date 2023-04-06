from abc import ABC
from abc import abstractmethod
from entities.ConsumptionDataType import ConsumptionDataType


class DataRepository(ABC):

    @abstractmethod
    def get_client_id_list(self) -> list[str]: pass
   
    @abstractmethod  
    def store_client_data(self, client_id:str, data: ConsumptionDataType) -> None: pass
   
    @abstractmethod
    def store_client_data_list(self, client_id:str, data_list: list[ConsumptionDataType]) -> None: pass
    
    @abstractmethod
    def get_client_data_list(self, client_id: str) -> list[ConsumptionDataType]: pass
    
    @abstractmethod   
    def get_all_data_list(self) -> list[ConsumptionDataType]: pass

    @abstractmethod   
    def get_souspicious_data_list(self) -> list[ConsumptionDataType]: pass

