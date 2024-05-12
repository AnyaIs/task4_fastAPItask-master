FROM python:3.11
RUN mkdir /fastapi_app
WORKDIR /fastapi_app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app

WORKDIR /fastapi_app

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

