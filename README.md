# FastApi-CRUD-API
A full-featured CRUD REST API built with FastAPI, SQLAlchemy, and PostgreSQL

# 🚀 FastAPI CRUD API (PostgreSQL)

A clean and practical CRUD REST API built using FastAPI and SQLAlchemy, backed by PostgreSQL
This project focuses on understanding backend fundamentals deeply — request flow, database interaction, and real-world API behavior.

This is not a tutorial copy.
This is learning by building

-------------------------------------------------------------------------------

🧠 What this project covers

This API implements full CRUD operations for a BankAccount resource:

* POST → Create a new user
* GET → Read user(s)
* PATCH → Partially update user data
* DELETE → Remove a user

Each operation is written with:

* Proper database session handling
* Safe existence checks
* Clean logic
* Real PATCH behavior (update only what is sent)

--------------------------------------------------------------------------------

🛠️ Tech Stack

* Python
* FastAPI
* SQLAlchemy (ORM)
* PostgreSQL
* Pydantic
* Uvicorn

--------------------------------------------------------------------------------

🧪 API Endpoints

➕ Create User

POST /users

📥 Get All Users

GET /users

🔍 Get User by ID

✏️  User (Partial Update)

PATCH /users/{user_id}

--------------------------------------------------------------------------------

Only the fields provided in the request are updated.
Missing fields are ignored — industry-style PATCH implementation

❌ Delete User

DELETE /users/{user_id}

-------------------------------------------------------------------------------
🔐 Key Learnings from this Project

* Difference between POST vs PATCH and GET VS POST
* Why "commit()" is required
* When to use "refresh()" (and when NOT to)
* How "Optional" fields enable partial updates
* How FastAPI dependency injection works
* How real CRUD APIs behave in production

--------------------------------------------------------------------------------

🧩 Database Model (Simplified)

BankAccount
- id (Primary Key)
- holdername
- age
- phone
- gmail
- pancard


-----------------------------------------------------------------------------

▶️ How to Run Locally

bash
pip install fastapi uvicorn sqlalchemy psycopg2
uvicorn main:app --reload

Make sure PostgreSQL is running and the database exists.

-----------------------------------------------------------------------------

⚠️ Note

This project is built for learning and practice purposes
Security features such as authentication, authorization, and environment variables can be added in future versions.

-----------------------------------------------------------------------------

📌 Future Improvements

* JWT Authentication
* Role-based access control
* Input validation rules
* Pagination & filtering
* Better error handling

-----------------------------------------------------------------------------

👨‍💻 Author
Ali shaikh- (Afridi)
    
  Backend Developer
    
Learning by building.
Logic over shortcuts.
Progress over perfection.

THANKS ❤️😊

