
from motor.motor_asyncio import AsyncIOMotorClient
from .core.config import setting


client =AsyncIOMotorClient(setting.MONGO_URL)
db=client(setting.DB_NAME)