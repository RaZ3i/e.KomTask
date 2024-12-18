from pydantic import BaseModel, EmailStr, field_validator


class InputData(BaseModel):
    # temp_name: str
    user_name: str | None = None
    user_phone: str | None = None
    user_email: str | None = None
    hire_date: str | None = None
