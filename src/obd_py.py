import obd
import logging


logger = logging.getLogger(__name__)

class OBDDevice():
    def __init__(self) -> None:
        self.connection = None
        self.initialise()

    def initialise(self):
        try:
            self.connection = obd.OBD()

        except AttributeError:
            logger.debug("No obd device has been detected")

    # def simulate_obd(self, command):




if __name__ == '__main__':
    obd_device = OBDDevice()