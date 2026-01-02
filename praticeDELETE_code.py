from fastapi import FastAPI, Depends , HTTPException
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel
from typing import Optional

engine = create_engine("postgresql://postgres:passwordxyz@localhost:5432/testdb" , echo=False)

SessionLocal = sessionmaker(bind=engine, autoflush=False,autocommit=False)

Base = declarative_base()

class BankAccount(Base):
    __tablename__ = "bank_info"
    id = Column(Integer, primary_key=True, autoincrement=True)
    holdername = Column(String)
    age = Column(Integer)
    phone = Column(Integer)
    gmail = Column(String)
    pancard = Column(Integer)
        
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
app = FastAPI()

@app.delete("/userdelete/{user_id}")
def delete_user(user_id : int , database : Session = Depends(get_db)):
    
    user = database.query(BankAccount).filter(BankAccount.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404 , detail= "SORRY USER NOT IN")
    
    database.delete(user)
    database.commit()
    
    return {"message" : "USER DELETE THANKS"}

