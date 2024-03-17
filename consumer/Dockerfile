FROM python:3.8-slim
COPY consumer.py /consumer.py
RUN pip install confluent-kafka clickhouse-driver
CMD ["python", "/consumer.py"]