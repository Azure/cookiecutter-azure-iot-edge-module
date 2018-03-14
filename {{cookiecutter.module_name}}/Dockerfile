FROM ubuntu:xenial

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python \
    python-pip \
    libboost1.58-all-dev \
    libcurl4-openssl-dev

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-u", "./main.py" ]