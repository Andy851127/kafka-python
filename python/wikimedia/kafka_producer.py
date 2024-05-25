from kafka import KafkaProducer
import json
import requests

# Kafka 生产者配置
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # JSON 序列化消息值
)

url = 'https://stream.wikimedia.org/v2/stream/recentchange'

response = requests.get(url, stream=True)

# 检查响应状态码
if response.status_code == 200:
    # 逐行迭代响应内容
    for line in response.iter_lines():
         producer.send('wikimedia',line.decode('utf-8'))
        # print("Message sent successfully.")
        # 解码每行数据并打印
else:
    # 请求失败，打印错误消息
    print(f"Failed to fetch data: {response.status_code}")
    producer.close()

