from entities.ConsumptionDataType import ConsumptionDataType
from ports.ConsumptionFileProcessor import ConsumptionFileProcessor
from use_cases.ConsumptionDataParserCSV import ConsumptionDataParserCSV

class ConsumptionFileProcessorCSV(ConsumptionFileProcessor, ConsumptionDataParserCSV):

    def __init__(self, filename: str):
        self.filename = filename

    def consumption_data(self) -> list[ConsumptionDataType]:
        import csv

        data = list() ##list[ConsumptionDataType]

        csv_handler = open(self.filename, newline='')
        csv_rows = csv.reader(csv_handler)
        headers = next(csv_rows)

        for csv_row in csv_rows:

            data.append(self.parse(csv_row))

        csv_handler.close()
        return data
 

