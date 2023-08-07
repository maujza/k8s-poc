from pydantic import BaseModel, StrictStr

class EncryptRequestModel(BaseModel):
    """Model for payload that is to be encrypted."""

    payload: StrictStr

    class Config:
        # Providing example usage for the model can be very helpful
        schema_extra = {"example": {"payload": "do_the_thing"}}


class Thing(BaseModel):
    """Model for the 'thing' which includes current time, 
    the encrypted payload, and an emoji.
    """

    current_time: StrictStr
    encrypted_payload: StrictStr
    emoji: StrictStr


class EncryptResponseModel(BaseModel):
    """Model for the response that includes 'thing'."""

    thing: Thing
