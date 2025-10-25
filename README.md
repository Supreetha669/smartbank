# smartbank
Backend Setup Steps 
-------------------------
Primary Use Cases to Pick (Backend-focused)
>>User Registration & KYC
 Customer signs up
 Uploads KYC documents
 Backend validates and stores user profile
Reason to pick: foundational functionality; demonstrates database, authentication, and file handling

>>Account Creation
  Customer requests a new account (Savings, Current, FD)
  Backend generates account number and validates initial deposit
  Reason to pick:  transactional logic, and API design
-----------------------------------------------------------------------------------------------------------
1.Created a virtual environment

I started by creating and activating a virtual environment in PyCharm to isolate dependencies.

2️. Installed core dependencies

I installed fastapi, uvicorn, sqlalchemy, psycopg2-binary, python-dotenv, passlib[bcrypt], and python-jose for JWT authentication.

3️.Configured environment variables

I created a .env file to securely store my database URL and JWT secret keys.

4️.Database connection setup

I configured SQLAlchemy ORM in a database.py file to connect FastAPI with the PostgreSQL database named smartbank.

5️.Created database models

I defined models such as User, Account, and Transaction using SQLAlchemy, each mapped to a database table.

6️.Built API routes

I created separate routers for each module — starting with user.py for registration and KYC, followed by account creation, transactions, and loans.

7️.Implemented security

I used bcrypt to hash passwords and JWT tokens for authentication and authorization.
Role-based access control was implemented for customers and admins.

8️.Tested API endpoints

I tested all API endpoints in Swagger UI (/docs) and Postman, verifying registration, login, and transaction flows.

9️.Ran the server

Finally, I launched the backend using:

uvicorn main:app --reload
