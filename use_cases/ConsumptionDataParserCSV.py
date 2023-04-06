from entities.ConsumptionDataType import ConsumptionDataType
from ports.ConsumptionDataParser import ConsumptionDataParser

class ConsumptionDataParserCSV(ConsumptionDataParser):

    def parse(self, csv_row) -> ConsumptionDataType:

        value = ConsumptionDataType()

        value.client_id = str(csv_row[0])
        value.period = str(csv_row[1])
        value.value = float(csv_row[2])

        return value

