from pathlib import Path
import pathlib
import datetime
from kafka_service import KafkaManager
import json






class ProcessManager:
    def __init__(self, kafka_producer:KafkaManager, directory_path:str):
        self.producer = kafka_producer
        self.path = Path(directory_path)
       
    def run(self):
        for file in self.path.iterdir():

            timestamp_ctime  = file.stat().st_ctime
            creation_time_datetime = str(datetime.datetime.fromtimestamp(timestamp_ctime))

            # Obtaining metadata and creating a structure for the information to be sent to Kafka
            file_data = {"file_path": file.as_posix(),
                    "metadata":{

                "file_name": file.name,
                "size_bytes":file.stat().st_size,
                "creation_time_datetime": creation_time_datetime
                
                }
            }

            try:        
                file_data = json.dumps(file_data)
                self.producer.produce("podcast",file_data,"data_of_podcasts")
                print(f"insert to kafka {file.name} file")
            except Exception as e:
                print(e)