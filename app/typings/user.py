from pydantic import BaseModel, model_validator
import json

class UserInfo(BaseModel):
    name: str
    email: str
    password: str
    gender: str

    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value