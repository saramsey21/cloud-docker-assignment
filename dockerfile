FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3

WORKDIR /usr/app/src

COPY script.py ./
COPY functions.py ./

ADD home/data/IF.txt home/data/IF.txt
ADD home/data/Limerick.txt home/data/Limerick.txt

ADD home/output/result.txt home/output/result.txt

CMD [ "python3", "./script.py"]