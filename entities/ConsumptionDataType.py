
class ConsumptionDataType(): 
    client_id:str
    period:str
    value:float
    average:float
    souspicious:bool

    def __init__(self, client_id:str = None, period:str = None, value:float = 0.0, average:float = 0.0, souspicious:bool = False):
        
        self.client_id = client_id
        self.period = period
        self.value = value
        self.average = average
        self.souspicious = souspicious

    def __eq__(self, other):
        return (self.client_id == other.client_id and
                self.period == other.period and
                self.value == other.value and
                self.average == other.average and
                self.souspicious == other.souspicious)