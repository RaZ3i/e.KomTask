from tinydb import TinyDB, Query
from copy import deepcopy

db = TinyDB("Forms_template.json", indent=4, separators=(",", ": "))
Template = Query()

templates = [
    {
        "temp_name": "EmployerForm_1",
        "user_name": "text",
        "user_phone": "phone",
        "user_email": "email",
        "hire_date": "date",
    },
    {
        "temp_name": "EmployerForm_2",
        "user_name": "text",
        "hire_date": "date",
    },
    {
        "temp_name": "EmployerForm_3",
        "user_name": "text",
        "user_phone": "phone",
        "user_email": "email",
    },
    {
        "temp_name": "EmployerForm_4",
        "user_name": "text",
    },
    {
        "temp_name": "EmployerForm_5",
        "user_name": "text",
        "user_email": "email",
        "hire_date": "date",
    },
]


class Config:

    @classmethod
    def create_db(cls):
        db.drop_table("_default")
        db.insert_multiple(templates)

    @classmethod
    def find_template(
        cls,
        types: list,
    ):
        types_without_none = {}
        for var in types:
            for k, v in var.items():
                if v is not None:
                    types_without_none.update({k: v})
        result = []
        data = db.search(
            (Template.user_name == types[3]["user_name"])
            | (Template.user_phone == types[1]["user_phone"])
            | (Template.user_email == types[2]["user_email"])
            | (Template.hire_date == types[0]["hire_date"]),
        )
        final_result = ""
        for res in deepcopy(data):
            res_for_compare = []
            for k, v in res.items():
                res_for_compare.append({k: v})
            res_for_compare.pop(0)
            count = 0
            for i in res_for_compare:
                if i in types:
                    count += 1
            if count == len(res_for_compare):
                result.append(db.get(doc_id=res.get("temp_name")[-1]))
        if len(result) == 1:
            final_result = result[0]["temp_name"]

        if len(result) > 1:
            arr_len = {}
            for res in result:
                arr_len.update({res.get("temp_name"): len(res) - 1})
            final_result = max(arr_len, key=arr_len.get)
        if len(result) == 0:
            final_result = types_without_none
        return final_result
