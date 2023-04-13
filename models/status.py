from pydantic import BaseModel

class Status(BaseModel):
    store_id:str
    status:str
    timestamp_utc:str