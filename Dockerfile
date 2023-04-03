FROM python:3.10

WORKDIR /app

COPY requirements/ /app/requirements/
COPY docker/docker-entrypoint.sh /app/

RUN pip install -r requirements/python/prod.txt

COPY . /app/

EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint.sh"]
