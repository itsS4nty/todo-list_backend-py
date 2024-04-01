from models import DutyStatus
from services.duty_service import deleteDuty, findDuties, insertDuty, updateDuty

def getDuties(status: DutyStatus | None):
    if(status is None):
        return None
    try:
        duties = findDuties(status)
        print(duties)
        sorted_duties = sorted(duties, key=lambda d: d['modified_at'])
        data = [{'id': d['id'], 'name': d['name']} for d in sorted_duties]
        return data
    except Exception as e:
        print('Err', e)
        return None
    
def addDuty(name: str):
    try:
        insertDuty(name)
        return True
    except:
        return False

def updDuty(id: int, status: DutyStatus):
    try:
        updateDuty(id, status)
        return True
    except:
        return False
    
def delDuty(id: int, full_delete: bool):
    try:
        deleteDuty(id) if full_delete else updateDuty(id, DutyStatus.DELETED.value)
        return True
    except:
        return False