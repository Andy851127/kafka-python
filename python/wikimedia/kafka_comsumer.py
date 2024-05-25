from kafka import KafkaConsumer
from pymongo import MongoClient
import json
import re

username = "root"  # 替换为你的MongoDB用户名
password = "root"  # 替换为你的MongoDB密码
host = "192.168.214.1"
port = 27018
authSource  = "admin"  # 默认的身份验证数据库是admin，替换为你的身份验证数据库

# Connect to MongoDB
client = MongoClient(
                      host
                     ,port
                     ,username = username
                     ,password = password
                     ,authSource  = authSource 
                    )  # assuming your MongoDB container is named 'mongodb'

# Get the database
db = client['wikimedia']
print("wikimedia db 建立完成!")

# Get the collection
collection = db['wikimedia_collection']
print("wikimedia collection 建立完成!")

# Kafka 消费者配置
consumer = KafkaConsumer(
            'wikimedia',  # 订阅的主题名称
            bootstrap_servers='kafka:9092',  # Kafka 服务器地址
            auto_offset_reset='earliest',  # 设置偏移量为最早可用的消息
            enable_auto_commit=True,  # 启用自动提交偏移量
            group_id='my_consumer_group',  # 消费者组 ID
            value_deserializer=lambda x: x.decode('utf-8')  # 消息值的反序列化函数
            )

# 消费消息
for message in consumer:
    try:
        result = message.value
        clean_result = '\n'.join(result.split('\\n'))
        clean_result = clean_result.replace('\\', '')
        
        # 修正 JSON 字符串，移除多餘的換行符和空格
        json_string = result.replace('\n', '').replace('  ', '')

        # 去掉字串最外層的引號
        clean_result = clean_result.strip('"')
        # 找到 "parsedcomment" 字符串的索引位置
        index_parsedcomment = clean_result.find('"parsedcomment"')

        # 截取字符串，保留 "parsedcomment" 之前的內容
        json_str = clean_result[:index_parsedcomment - 1]
        # # 添加末尾的 }
        json_str += "}"
        # # 使用切片操作去除最後一個逗號
        json_str_cleaned = json_str.rsplit(',', 1)[0] + json_str.rsplit(',', 1)[1].strip()
        print(json_str_cleaned)
        print(type(json_str_cleaned))

        message_dict = json.loads(json_str_cleaned)

        collection.insert_one(dict(message_dict))
    except:
        continue
# 关闭消费者连接
consumer.close()