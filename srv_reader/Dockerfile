FROM python:3.12-slim

COPY ./srv_reader /home/app
COPY ./data/100_sr.json /tmp/data/

WORKDIR /home/app

RUN pip3.12 install --upgrade pip
RUN pip3.12 install -r requirements.txt

CMD ["python3.12", "-u", "main.py"]