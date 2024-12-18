import pytest

# from tests.confest import test_client
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_chek_forms_1():
    response = client.post(
        "/get_form",
        params={
            "user_name": "Anton",
            "user_phone": "+7 213 432 12 32",
            "user_email": "uSer@sdv.eu",
            "hire_date": "12.12.2024",
        },
    )
    assert response.json() == "EmployerForm_1"


def test_chek_forms_2():
    response = client.post(
        "/get_form",
        params={
            "user_name": "Anton",
            "user_phone": "+7 213 432 12 32",
            "user_email": "uSer@sdv.eu",
            "hire_date": "2023-12-31",
        },
    )
    assert response.json() == "EmployerForm_1"


def test_chek_forms_3():
    response = client.post(
        "/get_form",
        params={
            "user_name": "Anton",
            "user_phone": "+7213 432 12 32",
            "user_email": "uSersdv.eu",
            "hire_date": "12/12/2024",
        },
    )
    assert response.json() == {
        "user_name": "text",
        "user_phone": "wrong phone",
        "user_email": "wrong email",
        "hire_date": "wrong date",
    }


def test_chek_forms_4():
    response = client.post(
        "/get_form",
        params={
            "user_name": "Anton",
            "hire_date": "2023-12-31",
        },
    )
    assert response.json() == "EmployerForm_2"


def test_chek_forms_5():
    response = client.post(
        "/get_form",
        params={
            "user_name": "Anton",
            "hire_date": "2023.12-31",
        },
    )
    assert response.json() == {
        "user_name": "text",
        "hire_date": "wrong date",
    }


def test_chek_forms_6():
    response = client.post(
        "/get_form",
        params={
            "user_name": "Anton",
        },
    )
    assert response.json() == "EmployerForm_4"


def test_chek_forms_7():
    response = client.post(
        "/get_form",
        params={
            "user_name": "Anton",
            "user_phone": "+7 213 432 12 32",
            "user_email": "uSer@sdv.eu",
        },
    )
    assert response.json() == "EmployerForm_3"


def test_chek_forms_8():
    response = client.post(
        "/get_form",
        params={
            "user_name": "Anton",
            "user_phone": "+7213 432 12 32",
            "user_email": "uSersdv.eu",
        },
    )
    assert response.json() == {
        "user_name": "text",
        "user_phone": "wrong phone",
        "user_email": "wrong email",
    }


def test_chek_forms_9():
    response = client.post(
        "/get_form",
        params={
            "user_name": "Anton",
            "user_email": "uSer@sdv.eu",
            "hire_date": "2023-12-31",
        },
    )
    assert response.json() == "EmployerForm_5"


def test_chek_forms_10():
    response = client.post(
        "/get_form",
        params={
            "user_name": "Anton",
            "user_phone": "+7 213 432 12 32",
            "hire_date": "2023-12-31",
        },
    )
    assert response.json() == "EmployerForm_2"
