from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for i in range(10):
    data = {"number": i}
    producer.send('your_topic_name', value=data)
    print(f'Sent: {data}')
    time.sleep(2)

producer.flush()

# from kafka import KafkaProducer
# import json

# producer = KafkaProducer(bootstrap_servers='localhost:9092')

# # Create the message as a dictionary
# message = {"number": 9}

# # Send the message to the Kafka topic
# producer.send('your_topic_name', value=json.dumps(message).encode('utf-8'))
# producer.flush()
