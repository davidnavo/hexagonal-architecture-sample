from ports.Finisher import Finisher

class FinisherOS(Finisher):
    def end(self, code:int) -> None:
        exit(code)