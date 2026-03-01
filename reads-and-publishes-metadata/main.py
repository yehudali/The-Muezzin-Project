import os
import logging

from config import  loading_environment_variables
from FolderManege import FolderManege
from kafka_service import KafkaManager
from logger import logger

def run():
    conf = loading_environment_variables(logger)

    kafka_producer = KafkaManager(conf.KAFKA_BOOTSTRAP_SERVERS, logger)
    foldermanege = FolderManege(conf.PATH_TO_DATA)




    



 

    # metadator = Metadator()
    # scema = SchemeManager()


    # list_of_files = foldermanege.get_list_file()

    # for file in list_of_files:
    #     metadata = metadator.get_matadata(file)

    











if __name__ == "__main__":
    run()