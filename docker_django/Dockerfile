FROM ubuntu:14.04
MAINTAINER Barend Fouché van Rooyen
EXPOSE 80

#set locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# debconf: unable to initialize frontend: Dialog
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get upgrade -y &&\
apt-get install -y python3.4-venv libpq-dev python3-dev phantomjs ;\
python3 -m venv /venv ;\
mkdir /app ;

ADD requirements.txt /app/
WORKDIR /app
RUN . /venv/bin/activate ;\
pip install -r requirements.txt ;\
deactivate
