from fastapi import FastAPI
from core.config import mount_static


app = FastAPI()

mount_static(app=app)

