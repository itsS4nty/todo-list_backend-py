from pydantic import BaseModel
from models import DutyStatus

class FindDutiesSchema(BaseModel):
    status: DutyStatus