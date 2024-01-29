FROM python:3.9

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt -y update && apt -y upgrade
RUN apt -y install \
		build-essential \
		python3-pip \
		python3-wheel \
		vim \
		git \
		tig \
		tmux \
		graphviz

RUN pip install --upgrade pip

COPY . /app
COPY requirements.txt .
WORKDIR /app

RUN pip install -r requirements.txt
