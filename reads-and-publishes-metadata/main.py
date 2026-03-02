import os
import logging

from config import  loading_environment_variables
from FolderManege import FolderManege
from kafka_service import KafkaManager
from logger import logger
from process_manager import ProcessManager

def run():
    conf = loading_environment_variables(logger)

    kafka_producer = KafkaManager(conf.KAFKA_BOOTSTRAP_SERVERS, logger)
    # foldermanege = FolderManege(conf.PATH_TO_DATA)

    process =ProcessManager(kafka_producer,conf.PATH_TO_DATA)
    process.run()



if __name__ == "__main__":
    run()