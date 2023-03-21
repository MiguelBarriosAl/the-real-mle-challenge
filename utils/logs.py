import datetime
import logging


class Logs:
    def __init__(self):
        self.timestamp = datetime.datetime.now()

    def info(self, data: str):
        message = f"{self.timestamp}: {data}"
        logging.info(message)

    def error(self, data_error: str):
        message = f"{self.timestamp}: Error : {data_error}"
        logging.error(message)