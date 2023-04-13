from pydantic import BaseModel

class TimeZone(BaseModel):
    store_id:str
    timezone_str:str