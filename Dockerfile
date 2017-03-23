FROM python:2.7
RUN apt-get update && pip install -r requirements.txt
