FROM python:3.10.8-alpine3.16
RUN apk update && \
    apk add --no-cache postgresql build-base && \
    pip install psycopg2-binary requests && \
    rm -rf /root/.cache/pip
WORKDIR src
COPY backup_restore.py /src/backup_restore.py
ENV ACCESS_TOKEN='' \
    DB_USER='postgres' \
    DB_USER_PASSWORD='' \
    DB_HOST='db' \
    DB_PORT='5432' \
    DB_NAME='tempdb'
CMD python3 /src/backup_restore.py
