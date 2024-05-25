from kafka import KafkaProducer
import json
import requests
import sseclient

# Kafka 生产者配置
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # JSON 序列化消息值
)

url = 'https://stream.wikimedia.org/v2/stream/recentchange'

def get_wikimedia_stream(url):
    # Open the connection to the stream
    response = requests.get(url, stream=True)
    
    # Check if the response is successful and contains a valid URL
    if response.ok and response.url:
        client = sseclient.SSEClient(response.url)  # Use response.url instead of url

        for event in client:
            if event.event == 'message':
                try:
                    # Parse the event data as JSON
                    change = json.loads(event.data)
                    json_data = json.dumps(change, indent=2)
                    # send producer comment
                    producer.send('wikimedia',json_data)
                except json.JSONDecodeError as e:
                    continue
                    
    else:
        print("Failed to establish connection to the stream.")
        producer.close()
        
if __name__ == "__main__":
    get_wikimedia_stream(url)