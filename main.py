from functools import lru_cache

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

import config
from accounts import models
from accounts.routers import authentication, users
from jobs.routers import jobs_routers
from database import engine


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers = ["Accept: application/json",
                   "Content-Type: application/json"],
    allow_credentials=["*"]

)


models.Base.metadata.create_all(bind=engine)

@lru_cache()
def get_settings():
    return config.Settings()

@app.get('/')
def root():
    context = {"Hello": "Api is working Fine"}
    return context

@app.get("/info")
def info(settings: config.Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
    }

app.include_router(users.router)
app.include_router(authentication.router)
app.include_router(jobs_routers.router)



