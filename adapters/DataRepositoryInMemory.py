
from ports.DataRepository import DataRepository
from entities.ConsumptionDataType import ConsumptionDataType


class DataRepositoryInMemory(DataRepository):
    
    def __init__(self):
        self.data_dict = dict()

    def get_client_id_list(self) -> list[str]:
        return list(self.data_dict.keys())
        
    def store_client_data(self, client_id:str, data: ConsumptionDataType) -> None:
        if not client_id in self.data_dict:
            self.data_dict[client_id] = list()
        self.data_dict[client_id].append(data)

    def store_client_data_list(self, client_id:str, data_list: list[ConsumptionDataType]) -> None:
        if not client_id in self.data_dict:
            self.data_dict[client_id] = list()
        self.data_dict[client_id] = data_list

    def get_client_data_list(self, client_id: str) -> list[ConsumptionDataType]: 
        if client_id in self.data_dict:
            return self.data_dict[client_id]
        raise Exception('No such client_id:' + client_id)
    
    def get_all_data_list(self) -> list[ConsumptionDataType]: 
        all_data = list()
        for client_id in self.data_dict:
            for data in self.data_dict[client_id]:
                all_data.append(data)
        return all_data
    
    def get_souspicious_data_list(self) -> list[ConsumptionDataType]: 
        souspicious_data = list()
        for client_id in self.data_dict:
            for data in self.data_dict[client_id]:
                if(data.souspicious):
                    souspicious_data.append(data)
        return souspicious_data
