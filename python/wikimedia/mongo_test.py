from pymongo import MongoClient

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
# client = MongoClient('mongodb://127.0.0.1:27017')  # assuming your MongoDB container is named 'mongodb'

# 尝试获取数据库列表以确认连接成功
db_list = client.list_database_names()
print("连接成功:", db_list)

# Get the database
db = client['wikimedia']

# Get the collection
collection = db['wikimedia_collection']

collection.insert_one({'apple':'3'})

print("建立成功!")