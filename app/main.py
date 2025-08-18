from fastapi import FastAPI
from core.config import mount_static
from api.v1.endpoints.users import router as user_router


app = FastAPI()

mount_static(app=app)
app.include_router(user_router)

