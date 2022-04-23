FROM python:3.9-alpine

WORKDIR /app

COPY . .

COPY requirements.txt /app/requirements.txt

# COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/manage_place_project/entrypoint.sh

RUN pip install -r requirements.txt

ENTRYPOINT [ "./app/manage_place_project/entrypoint.sh" ]


