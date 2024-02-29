from kafka import KafkaConsumer

from src.kafka_service.config import KAFKA_BOOTSTRAP_SERVERS
from src.kafka_service.utils import deserializer

consumer = KafkaConsumer(
    'messages',
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    auto_offset_reset='earliest',
    value_deserializer=deserializer
)
