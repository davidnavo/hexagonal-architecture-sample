##launch: python app.py 2016-readings.csv

import sys
import pprint

from adapters.ConsumptionFileProcessorFactory import ConsumptionFileProcessorFactory
from adapters.FinisherOS import FinisherOS
from adapters.LoggerStdOut import LoggerStdOut
from adapters.DataRepositoryInMemory import DataRepositoryInMemory

from use_cases.ConsumptionDataProcessor import ConsumptionDataProcessor

import traceback

logger = LoggerStdOut()    
consumption_file_processor_factory = ConsumptionFileProcessorFactory()
finisher = FinisherOS()

data_repository = DataRepositoryInMemory()
consumption_data_processor = ConsumptionDataProcessor()

def main(argv):

    try:
        consumptions_file:str = None

        try:
            consumptions_file = sys.argv[1]
        except:
            raise Exception('Please use right arguments: <file.xml> | <file.csv>')

        ##logger.log('Consumptions File:' + consumptions_file)

        consumption_file_processor = consumption_file_processor_factory.get(consumptions_file)
        clients_data = consumption_file_processor.consumption_data()
        
        for client_data in clients_data:
            data_repository.store_client_data(client_data.client_id, client_data)

        clients_id_list = data_repository.get_client_id_list()
        
        for client_id in clients_id_list:

            client_data_list = data_repository.get_client_data_list(client_id)
            client_data_list = consumption_data_processor.process(client_data_list)
            data_repository.store_client_data_list(client_id, client_data_list)

        souspicious_data_list = data_repository.get_souspicious_data_list()

        print(['Client', 'Month', 'Suspicious', 'Median'])
        for data in souspicious_data_list:
            print([data.client_id, data.period, data.value, data.average])
    
        ##logger.log('End')

        finisher.end(0)
            
    except Exception as e:
        logger.log(traceback.format_exc())
        finisher.end(-1)

    finisher.end(0)

if __name__ == "__main__":
    main(sys.argv[1:])

