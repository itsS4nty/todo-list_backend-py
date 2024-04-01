import time

import psycopg2
from models import DutyStatus
from database.connect import cursor

def findDuties(status: DutyStatus):
    try:
        cursor.execute("SELECT * FROM duties WHERE status = {status}".format(status=status))
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, row)) for row in cursor.fetchall()]
        return results
    except psycopg2.DatabaseError as e:
        print(e)
        return None

def insertDuty(name: str):
    now = time.time()
    try:
        cursor.execute("INSERT INTO duties VALUES (DEFAULT, '{name}', {status}, {created_at}, {modified_at})".format(
            name=name,
            status=DutyStatus.PENDING.value,
            created_at=now,
            modified_at=now,
        ))
        return True
    except psycopg2.DatabaseError as e:
        print(e)
        return False

def updateDuty(id: int, status: DutyStatus):
    _query = 'UPDATE duties SET status = {status}, modified_at = {modified_at} WHERE id = {id}'.format(
        id=id,
        status=status,
        modified_at=time.time()
    )
    try:
        print(_query)
        cursor.execute(_query)
        return True
    except psycopg2.DatabaseError as e:
        print(e)
        return False
    
def deleteDuty(id: int):
    try:
        cursor.execute('DELETE FROM duties WHERE id = {id}'.format(id=id))
        return True
    except psycopg2.DatabaseError as e:
        print(e)
        return False