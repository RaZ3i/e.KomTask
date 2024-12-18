import re
from pydantic import validate_email
from pydantic_core import PydanticCustomError


class Validators:

    @classmethod
    def __phone_validator(cls, phone: str):
        if phone is None:
            return None
        if not re.match(
            r"^(\+7)\s\d{3}\s\d{3}\s\d{2}\s\d{2}$",
            phone,
        ):
            return False
        return True

    @classmethod
    def __data_valdiator(cls, date_hr: str):
        if date_hr is None:
            return None
        if not re.match(
            r"^(3[01]|[12][0-9]|0?[1-9])(\.)(1[0-2]|0?[1-9])\2([0-9]{2})[0-9]{2}$",
            date_hr,
        ) and not re.match(
            r"^([0-9]{2})[0-9]{2}(-)(1[0-2]|0?[1-9])\2(3[01]|[12][0-9]|0?[1-9])$",
            date_hr,
        ):
            return False
        return True

    @classmethod
    def __email_validator(cls, email: str):
        try:
            if email is None:
                return None

            if validate_email(email):
                return True

        except PydanticCustomError:
            return False

    @classmethod
    def __chek_text(cls, text: str):
        if text is None:
            return None
        else:
            return True

    @classmethod
    def validate_input(cls, data):
        result = []

        if cls.__data_valdiator(data.hire_date) is False:
            result.append({"hire_date": "wrong date"})
        elif cls.__data_valdiator(data.hire_date) is None:
            result.append({"hire_date": None})
        else:
            result.append({"hire_date": "date"})
        if cls.__phone_validator(data.user_phone) is False:
            result.append({"user_phone": "wrong phone"})
        elif cls.__phone_validator(data.user_phone) is None:
            result.append({"user_phone": None})
        else:
            result.append({"user_phone": "phone"})
        if cls.__email_validator(data.user_email) is False:
            result.append({"user_email": "wrong email"})
        elif cls.__email_validator(data.user_email) is None:
            result.append({"user_email": None})
        else:
            result.append({"user_email": "email"})
        if cls.__chek_text(data.user_name) is None:
            result.append({"user_name": None})
        else:
            result.append({"user_name": "text"})
        res_without_none = {}
        for val in result:
            for k, v in val.items():
                if v is not None:
                    res_without_none.update({k: v})
        # for res in res_without_none:
        for k, v in res_without_none.items():
            if re.match(r"(wrong)\s\w+", v):
                final_res = {"success": False, "types": res_without_none}
                print(final_res)
                return final_res
        else:
            return {"success": True, "types": result}
