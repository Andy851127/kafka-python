# 使用 bitnami/kafka:3.4.1 作为基础镜像
FROM bitnami/kafka:3.4.1

# 切换到 root 用户
USER root

# 将 build.sh 复制到容器中的 /kafka 目录
COPY ./kafka/build_topics.sh /home/kafka/build_topics.sh

# 赋予 build.sh 执行权限
RUN chmod +x /home/kafka/build_topics.sh

# 切换回 Kafka 默认用户
USER 1001

# 在启动时执行 build.sh 脚本，然后启动 Kafka
CMD ["/bin/bash", "-c", "/opt/bitnami/scripts/kafka/run.sh && /home/kafka/build_topics.sh"]
