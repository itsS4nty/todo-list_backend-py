from pydantic import BaseModel
from models import DutyStatus

class UpdateDutySchema(BaseModel):
    id: int
    status: DutyStatus