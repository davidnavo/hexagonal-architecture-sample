from entities.ConsumptionDataType import ConsumptionDataType
from ports.ConsumptionDataParser import ConsumptionDataParser

class ConsumptionDataParserXML(ConsumptionDataParser):

    def parse(self, xml_row) -> ConsumptionDataType:
    
        value = ConsumptionDataType()

        value.client_id = str(xml_row.get('clientID'))
        value.period = str(xml_row.get('period'))
        value.value = float(xml_row.text)
            
        return value
