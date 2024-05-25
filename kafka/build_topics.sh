#!/bin/bash

# 等待 Kafka 服务启动
sleep 10

# build topic：wikimedia
kafka-topics.sh --bootstrap-server localhost:9092 --topic wikimedia --create --partitions 3