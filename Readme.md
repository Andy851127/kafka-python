# 於 python-kafka 路徑下，運行 Docker compose
docker compose up -d

# 查看 Docker conatainer
docker ps

# 進入 kafka 容器
docker exec -it <容器ID> /bin/bash

# 建立 wikimedia topic
kafka-topics.sh --bootstrap-server localhost:9092 --topic wikimedia --create --partitions 3

# 進入 python 容器
docker exec -it <容器ID> /bin/bash

# 執行 kafka_producer.py，接收 wikimedia streaming datas 到 kafka producer
cd wikimedia
python kafka_producer.py

# 執行 kafka_comsumer.py，接收 producer 資料，寫入 mongodb
cd wikimedia
python kafka_comsumer.py

# 執行 jupyter 使用 pyspark + pymongo + matplotlib + seaborn 做分析圖
點擊 /work/Statistical analysis chart.ipynb 運行 all cells