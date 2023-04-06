##launch: pytest test.py

import sys
import pprint

from adapters.ConsumptionFileProcessorFactory import ConsumptionFileProcessorFactory
from adapters.FinisherOS import FinisherOS
from adapters.LoggerStdOut import LoggerStdOut
from adapters.DataRepositoryInMemory import DataRepositoryInMemory
from entities.ConsumptionDataType import ConsumptionDataType

from use_cases.ConsumptionDataProcessor import ConsumptionDataProcessor

import traceback
import pytest

import unittest

class IntegrationTest(unittest.TestCase):

    def _consumption_files(self):
        return ['test.csv', 'test.xml']
    
    def _check_consumption_file_processor_classname(self, consumptions_file:str):
        classname = ''
        if(consumptions_file ==  'test.csv'): 
            classname = 'ConsumptionFileProcessorCSV'
        if(consumptions_file ==  'test.xml'): 
            classname = 'ConsumptionFileProcessorXML'
        return classname
    
    def _check_clients_id_list(self, consumptions_file:str):
        check_clients_id_list = list()
        if(consumptions_file ==  'test.csv'): 
            check_clients_id_list =  ['583ef6329d7b9']
        if(consumptions_file ==  'test.xml'): 
            check_clients_id_list = ['583ef6329e237']
        return check_clients_id_list

    def _check_client_data_list(self, consumptions_file:str):
        check_client_data_list = list()
        if(consumptions_file ==  'test.csv'): 
            check_client_data_list.append(ConsumptionDataType('583ef6329d7b9','2016-01',42451.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329d7b9','2016-02',44279.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329d7b9','2016-03',44055.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329d7b9','2016-04',40953.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329d7b9','2016-05',42566.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329d7b9','2016-06',41216.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329d7b9','2016-07',43597.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329d7b9','2016-08',43324.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329d7b9','2016-09',3564.0,  0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329d7b9','2016-10',44459.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329d7b9','2016-11',42997.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329d7b9','2016-12',42600.0, 0.0, False))
        if(consumptions_file ==  'test.xml'): 
            check_client_data_list.append(ConsumptionDataType('583ef6329e237', '2016-01', 30622.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329e237', '2016-02', 31072.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329e237', '2016-03', 29070.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329e237', '2016-04', 30056.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329e237', '2016-05', 31746.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329e237', '2016-06', 30560.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329e237', '2016-07', 32006.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329e237', '2016-08', 30209.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329e237', '2016-09', 30015.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329e237', '2016-10', 29554.0, 0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329e237', '2016-11', 1379.0,  0.0, False))
            check_client_data_list.append(ConsumptionDataType('583ef6329e237', '2016-12', 29597.0, 0.0, False))

        return check_client_data_list
    
    def _check_client_data_processed_list(self, consumptions_file:str):
        check_client_data_processed_list = list()
        if(consumptions_file ==  'test.csv'): 
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329d7b9','2016-01',42451.0, 39671.75, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329d7b9','2016-02',44279.0, 39671.75, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329d7b9','2016-03',44055.0, 39671.75, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329d7b9','2016-04',40953.0, 39671.75, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329d7b9','2016-05',42566.0, 39671.75, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329d7b9','2016-06',41216.0, 39671.75, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329d7b9','2016-07',43597.0, 39671.75, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329d7b9','2016-08',43324.0, 39671.75, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329d7b9','2016-09',3564.0,  39671.75,  True))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329d7b9','2016-10',44459.0, 39671.75, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329d7b9','2016-11',42997.0, 39671.75, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329d7b9','2016-12',42600.0, 39671.75, False))
        if(consumptions_file ==  'test.xml'): 
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329e237', '2016-01', 30622.0, 27990.5, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329e237', '2016-02', 31072.0, 27990.5, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329e237', '2016-03', 29070.0, 27990.5, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329e237', '2016-04', 30056.0, 27990.5, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329e237', '2016-05', 31746.0, 27990.5, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329e237', '2016-06', 30560.0, 27990.5, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329e237', '2016-07', 32006.0, 27990.5, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329e237', '2016-08', 30209.0, 27990.5, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329e237', '2016-09', 30015.0, 27990.5, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329e237', '2016-10', 29554.0, 27990.5, False))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329e237', '2016-11', 1379.0,  27990.5, True))
            check_client_data_processed_list.append(ConsumptionDataType('583ef6329e237', '2016-12', 29597.0, 27990.5, False))
        return check_client_data_processed_list
    
    def _check_souspicious_data_list(self, consumptions_file:str):
        check_souspicious_data_list = list()
        if(consumptions_file ==  'test.csv'): 
            check_souspicious_data_list = list()
            check_souspicious_data_list.append(ConsumptionDataType('583ef6329d7b9','2016-09',3564.0,  39671.75, True))
        if(consumptions_file ==  'test.xml'): 
            check_souspicious_data_list = []
            check_souspicious_data_list.append(ConsumptionDataType('583ef6329e237', '2016-11', 1379.0, 27990.5, True))
        return check_souspicious_data_list
       

    def test_integration(self):

        consumptions_files = self._consumption_files()

        for consumptions_file in consumptions_files:
            
            logger = LoggerStdOut()    
            consumption_file_processor_factory = ConsumptionFileProcessorFactory()
            finisher = FinisherOS()
            consumption_data_processor = ConsumptionDataProcessor()
            data_repository = DataRepositoryInMemory()

            check_consumption_file_processor_classname = self._check_consumption_file_processor_classname(consumptions_file)
            check_clients_id_list   = self._check_clients_id_list(consumptions_file)
            check_client_data_list =  self._check_client_data_list(consumptions_file)
            check_client_data_processed_list = self._check_client_data_processed_list(consumptions_file)
            check_souspicious_data_list = self._check_souspicious_data_list(consumptions_file)

            consumption_file_processor = consumption_file_processor_factory.get(consumptions_file)
            self.assertEqual(type(consumption_file_processor).__name__,check_consumption_file_processor_classname)

            clients_data = consumption_file_processor.consumption_data()
            pprint.pprint('CD-----------------------')
            for x in clients_data: pprint.pprint([x.client_id, x.period, x.value, x.average, x.souspicious])
            pprint.pprint('CCD-----------------------')
            for x in check_client_data_list: pprint.pprint([x.client_id, x.period, x.value,  x.average, x.souspicious])
            self.assertEqual(clients_data,check_client_data_list)  

            for client_data in clients_data:
                data_repository.store_client_data(client_data.client_id, client_data)

            clients_id_list = data_repository.get_client_id_list()
            self.assertEqual(clients_id_list, check_clients_id_list)
        
            for client_id in clients_id_list:

                client_data_list = data_repository.get_client_data_list(client_id)
                client_data_processed_list = consumption_data_processor.process(client_data_list)
                for x in client_data_processed_list: pprint.pprint([x.client_id, x.period, x.value, x.average, x.souspicious])
                for x in check_client_data_processed_list: pprint.pprint([x.client_id, x.period, x.value, x.average, x.souspicious])
                self.assertEqual(client_data_processed_list, check_client_data_processed_list)
                
                data_repository.store_client_data_list(client_id, client_data_processed_list)
                
                client_data_list = data_repository.get_client_data_list(client_id)
                self.assertEqual(client_data_list, check_client_data_processed_list)


            all_data_list = data_repository.get_all_data_list()
            self.assertEqual(all_data_list, check_client_data_processed_list)
            souspicious_data_list = data_repository.get_souspicious_data_list()

            ##for x in clients_data: pprint.pprint([x.client_id, x.period, x.value, x.average, x.souspicious])
            ##for x in check_client_data_list: pprint.pprint([x.client_id, x.period, x.value,  x.average, x.souspicious])
            self.assertEqual(souspicious_data_list, check_souspicious_data_list)


