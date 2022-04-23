FROM python:3.9-alpine

WORKDIR /app

COPY . .

COPY requirements.txt /app/requirements.txt

COPY entrypoint.sh /app/entrypoint.sh

RUN pip install -r requirements.txt

ENTRYPOINT [ "entrypoint.sh" ]