import obd
import logging

connection = obd.OBD()

class OBDConnection():
    def __init__(self) -> None:
        self.connection = None
        self.initialise()

    def initialise(self):
        try:
            self.connection = obd.OBD()

        except AttributeError :
            logging.log(1, "No obd device has been detected")

        
