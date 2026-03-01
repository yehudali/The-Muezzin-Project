from logging import Logger
import os
from dotenv import load_dotenv
load_dotenv()

class loading_environment_variables:
    def __init__(self, logger:Logger) -> None:
        self.logger = logger
        self.PATH_TO_DATA=os.getenv(r"ABSOLUTE_PATH_TO_DATA")
        self.KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
        self.Validate()

    def Validate(self):
        if not self.PATH_TO_DATA:
            self.logger.error("i don't hav a ABSOLUTE_PATH_TO_DATA env")
        if not self.KAFKA_BOOTSTRAP_SERVERS:
            self.logger.error("i don't hav a KAFKA_BOOTSTRAP_SERVERS env")
