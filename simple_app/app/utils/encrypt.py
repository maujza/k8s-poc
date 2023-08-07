import base64
import os
from simple_app.app.utils.logger import logger

from pyDes import CBC, PAD_PKCS5, des


def encrypt_data(data: str, password: str) -> str:
    try:
        iv = os.urandom(8)
        encryptor = des(password, CBC, iv, pad=None, padmode=PAD_PKCS5)
        encrypted_data = encryptor.encrypt(data)
        encrypted_data = base64.b64encode(encrypted_data)
        return encrypted_data.decode("UTF-8")
    except Exception as e:
        logger.error(f"An error occurred during encryption: {e}")
        raise
