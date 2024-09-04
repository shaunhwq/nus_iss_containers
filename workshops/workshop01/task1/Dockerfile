FROM python:3.10-slim

ENV PORT=5000
ENV INSTANCE_NAME="Test"
ENV INSTANCE_HASH="test2"

COPY app app
WORKDIR app

RUN pip install -r requirements.txt

ENTRYPOINT ./run.sh
