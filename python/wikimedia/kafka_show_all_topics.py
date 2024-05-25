from kafka.admin import KafkaAdminClient, NewTopic, ConfigResource

# create client
admin_client = KafkaAdminClient(bootstrap_servers='kafka:9092')

current_topics = admin_client.list_topics()

print("current_topics:",current_topics)

# close client
admin_client.close()