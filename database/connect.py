import os
from dotenv import load_dotenv 
import psycopg2

load_dotenv()

try:
    conn = psycopg2.connect(
        database=os.getenv('PSQL_DATABASE'),
        host=os.getenv('PSQL_HOST'),
        user=os.getenv('PSQL_USER'),
        password=os.getenv('PSQL_PASSWORD'),
        port=os.getenv('PSQL_PORT')
    )
    conn.autocommit = True
    cursor = conn.cursor()
    print('Success')
except:
    print('Error')
