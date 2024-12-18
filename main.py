from typing import Annotated

import uvicorn
from fastapi import FastAPI, Query
from schemas import InputData
from db import Config
from validators import Validators

app = FastAPI(title="TestCase")
Config.create_db()


@app.post(
    "/get_form",
)
def chek_forms(data: Annotated[InputData, Query(title="Query string")]):
    valid_res = Validators.validate_input(data=data)
    print(valid_res)
    if valid_res["success"] is False:
        template_result = valid_res["types"]
        return template_result
    else:
        types = valid_res["types"]

        template_result = Config.find_template(
            types=types,
        )
        return template_result


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
