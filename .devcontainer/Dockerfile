FROM alpine:latest

LABEL MAINTAINER = "Fedorov"

# 替换apk使用的源
COPY repositories /etc/apk/repositories
COPY requirements.txt /root/requirements.txt

# Install required packages and remove the apt packages cache when done.
# RUN apk update 
RUN apk add python3 \
	python3-dev \
	gcc \
	g++ \
	py3-pip

RUN pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/

RUN pip3 install --no-cache-dir -r /root/requirements.txt

# 添加/root/.local/bin目录到环境变量
# ENV PATH="/root/.local/bin:${PATH}"

# RUN  rm -r /root/.cache

# copy all the configfiles
# COPY default.conf /etc/nginx/http.d/default.conf
# COPY yuejuan.ini /etc/supervisor.d/
# xadmin针对python3.10的cache源文件修改
# COPY cache.py /usr/lib/python3.10/site-packages/django/views/decorators/cache.py

# EXPOSE 8080

# CMD ["supervisord", "-n", "-c", "/etc/supervisord.conf"]
CMD [ "pip list" ]