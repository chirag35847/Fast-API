from fastapi import FastAPI
from routes.user import user
from routes.api import api
app = FastAPI()

app.include_router(user)
app.include_router(api)
