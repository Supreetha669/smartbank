import pytest
from fastapi.testclient import TestClient
from main import app
from database import Base, engine, SessionLocal
from models import User, Account

client = TestClient(app)

# Use a separate test database
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://bankuser:password123@localhost:3306/smartbankdb"

@pytest.fixture(scope="module")
def db_setup():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

def test_register_user(db_setup):
    response = client.post(
        "/user/register",
        json={"username": "testuser", "email": "testuser@example.com", "password": "secure123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "user_id" in data
    assert data["message"] == "User registered successfully"

def test_create_account(db_setup):
    # First, register a new user
    response_user = client.post(
        "/user/register",
        json={"username": "accountuser", "email": "accountuser@example.com", "password": "secure123"}
    )
    user_id = response_user.json()["user_id"]

    # Now create account
    response_account = client.post(
        "/account/create",
        json={"user_id": user_id, "account_type": "Savings", "initial_deposit": 2000}
    )
    data = response_account.json()
    assert response_account.status_code == 200
    assert "account_number" in data
    assert data["message"] == "Account created successfully"
