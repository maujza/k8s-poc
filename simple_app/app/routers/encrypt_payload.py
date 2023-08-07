import os
from datetime import datetime, timezone

from fastapi import APIRouter, Depends
from simple_app.app.models.encrypt_model import EncryptRequestModel
from simple_app.app.utils.encrypt import encrypt_data
from simple_app.app.utils.get_emojis import get_smile_emoji
from simple_app.app.utils.logger import logger


router = APIRouter(tags=["encrypt_payload"])

pwd = os.getenv("ENCRYPT_PWD")

def get_encrypted_data(data: str) -> str:
    encrypted_data = encrypt_data(data=data, password=pwd)
    logger.info("Data encrypted successfully.")
    return encrypted_data

def get_current_time() -> str:
    current_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    logger.info("Current time fetched successfully.")
    return current_time

def get_emoji() -> str:
    emoji = get_smile_emoji("./simple_app/app/utils/emoji.json")
    if emoji:
        logger.info("Emoji fetched successfully.")
    else:
        logger.warning("Failed to fetch emoji.")
    return emoji

@router.post("/encrypt_payload", status_code=200)
async def encrypt_payload(request: EncryptRequestModel):
    body = request.dict()
    data_encrypted = get_encrypted_data(body["payload"])
    response = {
        "thing": {
            "current_time": get_current_time(),
            "encrypted_payload": data_encrypted,
            "emoji": get_emoji(),
        }
    }
    logger.info("Response prepared successfully.")
    return response

