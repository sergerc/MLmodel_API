FROM ubuntu

ADD . /accidentes_api

WORKDIR /accidentes_api


RUN apt-get update && apt-get install python3.6 -y && apt-get install python3-pip -y
RUN apt-get install vim -y
RUN pip3 install -r requirements.txt


CMD ["/bin/bash"]