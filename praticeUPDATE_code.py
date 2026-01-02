from fastapi import FastAPI, Depends, HTTPException 
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel
from typing import Optional

engine = create_engine("postgresql://postgres:passwordxyzzz@localhost:5432/testdb" , echo=False)

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()

class BankAccount(Base):
    __tablename__ = "bank_info"
    id = Column(Integer, primary_key=True, autoincrement=True)
    holdername = Column(String)
    age = Column(Integer)
    phone = Column(Integer)
    gmail = Column(String)
    pancard = Column(Integer)
    
class Secureinfo(BaseModel):
    holdername : Optional[str] = None
    age : Optional[int] = None
    phone: Optional[int] = None
    gmail : Optional[str] = None
    
    class Config:
        from_attributes = True
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
app = FastAPI()

@app.patch("/userpatch/{user_id}" , response_model=Secureinfo)
def patch_userget(user_id : int , userreq : Secureinfo , database : Session = Depends(get_db)):
    
    databuser = database.query(BankAccount).filter(BankAccount.id == user_id).first()
    
    if not databuser:
        raise HTTPException(status_code=404 , detail="User not Found")
    
    if userreq.holdername is not None: 
        databuser.holdername = userreq.holdername
        
    if userreq.age is not None:
        databuser.age = userreq.age 
        
    if userreq.phone is not None:
        databuser.phone = userreq.phone
    
    if userreq.gmail is not None:
        databuser.gmail = userreq.gmail
        
    database.commit()
    database.refresh(databuser)
        
    return databuser