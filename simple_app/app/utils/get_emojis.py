import json
from typing import Optional
from simple_app.app.utils.logger import logger

def get_smile_emoji(path: str) -> Optional[str]:
    try:
        with open(path, "r") as emojis:
            all_emojis = json.load(emojis)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"An error occurred while trying to load emojis: {e}")
        return None

    for emoji in all_emojis:
        if emoji["name"] == "SMILING FACE WITH OPEN MOUTH AND SMILING EYES":
            smile_emoji = emoji["unified"]
            return "".join([chr(int(code, 16)) for code in smile_emoji.split("-")])

    logger.info("Smile emoji was not found in the provided file.")
    return None
