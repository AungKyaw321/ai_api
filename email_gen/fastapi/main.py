from fastapi import FastAPI, HTTPException, Depends, status
from typing import Annotated, Dict
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from models import Base, SavedEmail
from database import engine, SessionLocal
from generation import generate_newsletter
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()
Base.metadata.create_all(bind=engine)

class PostBase(BaseModel):
    company_a: Dict[str, str]
    company_b: Dict[str, str]
    company_c: Dict[str, str]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/email/", status_code=status.HTTP_201_CREATED)
async def create_email(email: PostBase, db: db_dependency):
    company_a = email.company_a
    company_b = email.company_b
    company_c = email.company_c

    base64encoded_email = generate_newsletter(company_a, company_b, company_c)

    db_email = SavedEmail(base64_html=base64encoded_email)
    db.add(db_email)
    db.commit()
    db.refresh(db_email)

    return db_email

@app.get("/email/")
def get_email_by_date(date: str, db: Session = Depends(get_db)):
    try:
        query_date = datetime.strptime(date, "%m/%d/%Y")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use MM/dd/yyyy")

    email = db.query(SavedEmail).filter(func.date(SavedEmail.created_date) == query_date.date()).first()

    if not email:
        raise HTTPException(status_code=404, detail="No email found for the given date")

    return {
        "id": email.id,
        "base64_html": email.base64_html,
        "created_date": email.created_date.strftime("%m/%d/%Y")
    }
