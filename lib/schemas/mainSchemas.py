from lib.schemas.models.findDuties import FindDutiesSchema
from lib.schemas.models.updateDuty import UpdateDutySchema

schemas = {
    "FindDuties": FindDutiesSchema,
    "UpdateDuties": UpdateDutySchema
}

def validateSchema(schemaId, data):
    try:
        print(data)
        schemas[schemaId].model_validate({"status": data})
        return data
    except:
        print('Error')
        return None