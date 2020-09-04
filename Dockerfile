FROM python:3-alpine

MAINTAINER Ryan Aquino

RUN set -e; \
        apk add --no-cache --virtual .build-deps \
                gcc \
                libc-dev \
                linux-headers \
                mariadb-dev \
                python3-dev \
                postgresql-dev \
        ;

COPY . /app

WORKDIR /app

RUN pip install pipenv

RUN pipenv lock --requirements > requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
