from copy import copy, deepcopy
from entities.ConsumptionDataType import ConsumptionDataType

class ConsumptionDataProcessor:

    @classmethod
    def get_average(cls, data_list: list[ConsumptionDataType], clientId):
        average = 0

        value_accumulator = 0
        value_counter = 0
        
        for data in data_list:
            if(data.client_id == clientId):
                value_accumulator += data.value
                value_counter += 1

        if(value_counter > 0):
            average = float(value_accumulator) / float(value_counter)

        return average
            
    @classmethod
    def set_average(cls, processed_data: ConsumptionDataType, average:float):

        processed_data.average = average

    @classmethod
    def get_souspicious(cls, data:ConsumptionDataType, average:float):

        if(data.value > average * 1.5 or data.value < average * 0.5 ):
            return True
        
        return False
           
    @classmethod
    def set_souspicious(cls, processed_data: ConsumptionDataType, souspicious:bool):

        processed_data.souspicious = souspicious

    @classmethod
    def process(cls, data_list: list[ConsumptionDataType]):
        processed_data_list = list()

        for data in data_list:

            processed_data = copy(data)

            average = cls.get_average(data_list, processed_data.client_id)
            cls.set_average(processed_data, average)
            
            souspicious = cls.get_souspicious(processed_data, average)
            cls.set_souspicious(processed_data, souspicious)

            processed_data_list.append(processed_data)
                
        return processed_data_list    

    
 

    


            
