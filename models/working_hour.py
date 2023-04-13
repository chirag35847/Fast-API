from pydantic import BaseModel

class WorkingHour(BaseModel):
    store_id:int
    day:int 
    start_time_local:str
    end_time_local:str