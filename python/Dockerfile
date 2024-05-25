# 使用官方 Python 镜像作为基础镜像
FROM python:3.8.10

# 将当前目录下的 requirements.txt 复制到容器中的 home/python 目录
COPY ./python/requirements.txt /home/python/requirements.txt

# 切换到 /home/python 目录
WORKDIR /home/python

# 更新 pip
RUN python -m pip install --upgrade pip

# 安装 requirements.txt 中的包
RUN pip install -r requirements.txt

# 保持容器运行
CMD ["tail", "-f", "/dev/null"]
