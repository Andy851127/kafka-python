# 運行 Dockerfile
docker build -t kafka:3.7.0 .

# 查看 Docker image
docker images

# 刪除 Docker image
docker rmi kafka

# 運行 Docker 
docker run -it --rm kafka:3.7.0 /bin/bash

# 驗證 Docker 執行狀況
docker ps

# 刪除不要的 Container
docker rm <容器ID>

# 進入容器
docker exec -it <容器ID> /bin/bash
