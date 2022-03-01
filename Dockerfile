FROM ubuntu:bionic


RUN apt-get update 
RUN apt-get install -y python3 python3-pip 
RUN apt-get install -y wget
RUN apt-get install -y curl

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

ENV DISPLAY=:99

USER root

COPY . /pedro
WORKDIR /pedro

ENV LANG C.UTF-8
RUN pip3 install -U pip setuptools 
RUN pip3 install -r requirements.txt


CMD python3 -u src/app.py

