import json
import logging
import sys
import time

from kafka import KafkaConsumer
from location_service import create_location

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("location-service")
BOOTSTRAP_SERVERS = ['kafka-service:9092']


def get_kafka_object(timeout=2500):
    i = 0
    while True:
        time.sleep(3)
        if i > timeout:
            logger.info("system timedout")
            sys.exit()
        try:
            return KafkaConsumer('location',
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=False,
                                 value_deserializer=lambda m:
                                 json.loads(m.decode('utf-8')),
                                 bootstrap_servers=BOOTSTRAP_SERVERS)
        except Exception:
            logger.info("loading Kafka")
            i += 1


def serve():
    consumer = get_kafka_object()
    for message in consumer:
        logger.log(logging.INFO, 'Received a new location={}.'.format(message.value))
        create_location(message.value)



if __name__ == "__main__":
    serve()
