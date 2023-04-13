from fastapi import APIRouter
from models.timezone import TimeZone
from models.status import Status
from models.working_hour import WorkingHour
from config.db import workingHr,status,timezone
from schemas.schema import seralizeDict,seralizeList
import bson
import pymongo
from datetime import datetime,timedelta
import pytz

import pandas as pd

api = APIRouter()

@api.get('/trigger_report')
def find_max_time():
    maxTime =  seralizeDict(status.find_one(sort=[('timestamp_utc',pymongo.DESCENDING)]))['timestamp_utc']

    oneHour=maxTime-timedelta(minutes=60)
    oneDay=maxTime-timedelta(days=1)
    oneWeek=maxTime-timedelta(days=7)

    # return {maxTime,oneHour,oneDay,oneWeek}
    allStoreId=[]
    # for doc in status.find().distinct('store_id'):
    doc = 1481966498820158979
    curTimeZone = timezone.find_one({'store_id':doc})
    if curTimeZone is None:
        curTimeZone = 'America/Chicago'
    else:
        curTimeZone = curTimeZone['timezone_str']
        
    local = pytz.timezone(curTimeZone)
    curWorkingHr = workingHr.find({'store_id':doc})
    curWorkingHr = seralizeList(curWorkingHr)
    print(curWorkingHr)
    
    return curWorkingHr
    # return allStoreId
