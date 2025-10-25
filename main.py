from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from db import init_db, get_db
from models import User, Account
from utils import hash_password, generate_account_number

init_db()
app = FastAPI(title="SmartBank")

@app.post("/register")
def register(username: str, email: str, password: str, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(username=username, email=email, password_hash=hash_password(password), kyc_status="Pending")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully", "user_id": new_user.id, "kyc_status": new_user.kyc_status}

@app.post("/create_account")
def create_account(user_id: int, account_type: str, initial_deposit: float, db: Session = Depends(get_db)):
    if initial_deposit < 500:
        raise HTTPException(status_code=400, detail="Initial deposit must be at least 500")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    account = Account(user_id=user_id, account_type=account_type, account_number=generate_account_number(), balance=initial_deposit)
    db.add(account)
    db.commit()
    db.refresh(account)
    return {"message": "Account created successfully", "account_number": account.account_number, "balance": account.balance}