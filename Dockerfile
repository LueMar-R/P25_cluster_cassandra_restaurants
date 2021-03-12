FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install fastapi uvicorn cassandra-driver

COPY ./app /app