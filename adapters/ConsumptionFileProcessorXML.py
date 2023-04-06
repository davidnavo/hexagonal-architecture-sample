
from entities.ConsumptionDataType import ConsumptionDataType
from ports.ConsumptionFileProcessor import ConsumptionFileProcessor
from use_cases.ConsumptionDataParserXML import ConsumptionDataParserXML

class ConsumptionFileProcessorXML(ConsumptionFileProcessor, ConsumptionDataParserXML):

    def __init__(self, filename: str):
        self.filename = filename

    def consumption_data(self) -> list[ConsumptionDataType]:
        import xml.etree.ElementTree as ET
        
        data = list() ##list[ConsumptionDataType]

        tree = ET.parse(self.filename)
        root = tree.getroot()

        for xml_row in root.findall('./reading'): 
            data.append(self.parse(xml_row))

        return data