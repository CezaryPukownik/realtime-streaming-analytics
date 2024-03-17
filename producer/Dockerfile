FROM python:3.8-slim
COPY producer.py /producer.py
RUN pip install confluent-kafka
CMD ["python", "/producer.py"]