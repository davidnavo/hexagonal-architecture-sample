
import pathlib
from adapters.ConsumptionFileProcessorCSV import ConsumptionFileProcessorCSV
from adapters.ConsumptionFileProcessorXML import ConsumptionFileProcessorXML
from ports.Factory import Factory

import pprint

class ConsumptionFileProcessorFactory(Factory):
 
    @classmethod
    def get(classname, filename: str):
        import pathlib

        file_extension = pathlib.Path(filename).suffix.upper()
        file_exists =  pathlib.Path(filename).is_file()

        if file_exists and file_extension == ".XML": return ConsumptionFileProcessorXML(filename)
        if file_exists and file_extension == ".CSV": return ConsumptionFileProcessorCSV(filename)
        raise Exception("Bad consumption data file: " + filename)