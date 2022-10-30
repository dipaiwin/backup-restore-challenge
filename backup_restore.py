import os
import requests
import base64
from subprocess import run, PIPE, Popen
import psycopg2
from json import dumps

BASE_URL = "https://hackattic.com/challenges/backup_restore"

# Read envs
access_token = os.getenv("ACCESS_TOKEN")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_USER_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Create the connection string for psql command
psql_conn = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}"

# Get dump and store it as bin file
resp = requests.get(f"{BASE_URL}/problem?access_token={access_token}").json()
dump = base64.b64decode(resp['dump'])
with open("./data.dump", "wb") as f:
    f.write(dump)

# Restore dump to a temp db
run(["psql", psql_conn,  "-c", "create database tempdb;"])
gunzip = Popen(["gunzip", "-c", "./data.dump"], stdout=PIPE)
run(["psql", f"{psql_conn}/{db_name}"], stdin=gunzip.stdout)

# Connect to the db and select data where status='alive'
with psycopg2.connect(f"dbname={db_name} host={db_host} port={db_port} password={db_password} user={db_user}") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT ssn FROM criminal_records where status='alive';")
    ssn = cursor.fetchall()
    result = [item[0] for item in ssn]

# Send results
data = dumps({"alive_ssns": result})
post_request = requests.post(f"{BASE_URL}/solve?access_token={access_token}", data=data)
print(post_request.text)
