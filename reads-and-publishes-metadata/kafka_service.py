from confluent_kafka import Producer
from logging import Logger

class KafkaManager:
    def __init__(self,bootstrap_servers, logger:Logger) -> None:
        self.logger = logger
        self.bootstrap_servers = bootstrap_servers
        self.config = {
            "bootstrap.servers":self.bootstrap_servers,
            "client.id": "reads-and-publishes-metadata",
            'acks': 'all',
            'retries': 3
        }

        self.producer = Producer(self.config)
        

    def acked(self ,err, msg):
        if err is not None:
            self.logger.error("Failed to deliver message: %s: %s" % (str(msg), str(err)))
        else:
            self.logger.info("Message produced: %s" % (str(msg)))

    def produce(self, kay:str,value:str, topic_name):
        try:
            value_to_kafka = value.encode()
            kay_to_kafka = kay.encode()
            self.topic_name = topic_name
            self.producer.produce(self.topic_name, key=kay_to_kafka, value= value_to_kafka,callback=self.acked)
            self.producer.poll(0.1)

            
        except Exception as e:
            self.logger.error(f"error while produce to kafka: {e}")


