from pydantic import BaseModel
from enum import Enum


class DutyStatus(Enum):
    PENDING = 0
    DONE = 1
    DELETED = 2

class Duty(BaseModel):
    id: int
    name: str
    status: DutyStatus
    created_at: int
    modified_at: int
    
    
class CreateDuty(BaseModel):
    name: str
    
class UpdateDuty(BaseModel):
    id: int
    status: int

class DeleteDuty(BaseModel):
    id: int
    fullDelete: bool