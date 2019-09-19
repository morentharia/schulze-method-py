FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN \
        apt-get update -y && \
        apt-get install python3-numpy python3-pandas && \
        pip install -r requirements.txt

COPY ./app /app
