import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_data():
    response = client.get("/api/data")
    assert response.status_code == 200

    data = response.json()
    data = data["data"]
    assert "csv" in data
    assert "pptx" in data
    assert "json" in data
    assert "pdf" in data


def test_get_data_csv():
    response = client.get("/api/data/csv")
    assert response.status_code == 200


def test_get_data_pptx():
    response = client.get("/api/data/pptx")
    assert response.status_code == 200


def test_get_data_json():
    response = client.get("/api/data/json")
    assert response.status_code == 200


def test_get_data_pdf():
    response = client.get("/api/data/pdf")
    assert response.status_code == 200


def test_get_data_not_found():
    response = client.get("/api/data/unknown_type")
    assert response.status_code == 404
