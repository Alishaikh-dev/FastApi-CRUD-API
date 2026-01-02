from fastapi import FastAPI, Depends ,HTTPException
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel

# START 👀 DEFINE AND CONNECTION SETUP
engine = create_engine("postgresql://postgres:passwordxyzzz@localhost:5432/testdb" , echo=False)

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
    
class Secureinfo(BaseModel):
    holdername : str
    age : int
    phone : int
    
    class Config:
        from_attributes = True
            
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# END 👀 DEFINE AND CONNECTION SETUP  
#------------------------------------------------------------

# APP AND END POINTSETUP 
app = FastAPI()

#GET ALL USERS INFO 
@app.get("/userget", response_model=list[Secureinfo])
def get_all_users(database : Session = Depends(get_db)):
    info = database.query(BankAccount).all()
    return info

#GET ALL USERS USING ID 
@app.get("/usersget/{user_id}" , response_model=Secureinfo)
def get_id_user(user_id : int , database : Session = Depends(get_db)):
    userid = database.query(BankAccount).filter(BankAccount.id == user_id).first()
    
    if not userid:
        raise HTTPException(status_code=404 , detail="User not found sorry")
    return userid
