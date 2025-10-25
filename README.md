SmartBank

A modular backend system for banking operations using FastAPI, SQLAlchemy, and MySQL.

Supports:

User registration with simulated KYC

Account creation with validation and generated account numbers

Tech Stack

Python 3.11+

FastAPI

SQLAlchemy

MySQL

PyMySQL

bcrypt

Uvicorn

Project Structure
smartbank_backend/
│
├── main.py
├── models.py
├── db.py
├── utils.py
├── requirements.txt

Setup Instructions
1. Clone the repository
git clone <your-repo-url>
cd smartbank_backend

2. Set up MySQL
CREATE DATABASE bankdb;
CREATE USER 'bankuser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password123';
GRANT ALL PRIVILEGES ON bankdb.* TO 'bankuser'@'localhost';
FLUSH PRIVILEGES;

3. Install dependencies
pip install -r requirements.txt
pip install cryptography

4. Run the FastAPI server
uvicorn main:app --reload --host 127.0.0.1 --port 8000


Swagger UI: http://127.0.0.1:8000/docs

API Endpoints
1. Register User

POST /register

Body:

{
  "username": "John",
  "email": "john@example.com",
  "password": "secure123"
}


Response:

{
  "message": "User registered successfully",
  "user_id": 1,
  "kyc_status": "Pending"
}

2. Create Account

POST /create_account

Body/Query:

{
  "user_id": 1,
  "account_type": "Savings",
  "initial_deposit": 2000
}


Response:

{
  "message": "Account created successfully",
  "account_number": "1234567890",
  "balance": 2000
}


Validation: minimum deposit 500, must use existing user_id

Testing

Swagger UI: http://127.0.0.1:8000/docs

Curl commands:

curl -X POST "http://127.0.0.1:8000/register" -d "username=John&email=john@example.com&password=secure123"

curl -X POST "http://127.0.0.1:8000/create_account?user_id=1&account_type=Savings&initial_deposit=2000"


Check MySQL tables:

SELECT * FROM users;
SELECT * FROM accounts;
