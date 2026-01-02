from fastapi import FastAPI, Depends
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel

# START 👀 DEFINE AND CONNECTION SETUP
engine = create_engine("postgresql://postgres:passwordxyzzz@localhost:5432/testdb")

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
    
Base.metadata.create_all(engine)
    
class JsonApi(BaseModel):
    holdername : str
    age : int
    phone : int
    gmail : str
    pancard : int
    
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

@app.post("/Acount") 
def create_user(userx : JsonApi , database : Session= Depends(get_db)):
    
    new_user = BankAccount(
        holdername = userx.holdername,
        age = userx.age,
        phone = userx.phone,
        gmail = userx.gmail,
        pancard = userx.pancard
        
        )

    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user
       