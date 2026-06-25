from fastapi.testclient import TestClient
from app.main import app
import pytest
from app.core.db import Base, engine

@pytest.fixture(autouse=True)
def clean_database():
    yield
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_register_user():
    response = client.post("/auth/register", json={
        "email": "testuser1@example.com",
        "password": "testuser1234"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "testuser1@example.com"

def test_duplicate_user():
    # First registration should succeed
    client.post("/auth/register", json={
        "email": "testuser1@example.com",
        "password": "testuser1234"
    })
    # Second registration of same email should fail
    response = client.post("/auth/register", json={
        "email": "testuser1@example.com",
        "password": "testuser1234"
    })
    assert response.status_code == 400
    client.post("/auth/register", json={
        "email": "testuser1@example.com",
        "password": "testuser1234"
    })
    assert response.status_code == 400

def test_login_success():
    client.post("/auth/register", json={
        "email": "testuser3@example.com",
        "password": "test1234"
    })
    response = client.post("/auth/login", json={
        "email": "testuser3@example.com",
        "password": "test1234"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_wrong_password():
    response = client.post("/auth/login", json={
        "email": "testuser3@example.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401