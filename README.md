💰 Python Finance Tracking Backend (FastAPI)

A clean and modular backend system for managing personal financial data, built using FastAPI, SQLAlchemy, and SQLite.
This project demonstrates strong backend fundamentals including API design, data handling, role-based access, and financial analytics.

🚀 Project Overview

This application allows users to:

Manage income and expense transactions
Analyze financial data through summaries
Access features based on user roles (viewer, analyst, admin)

It is designed as a backend service that can power a finance dashboard or application.

✨ Features
💰 Transaction Management
Create, update, delete financial records
View all transactions
Filter by:
Type (income / expense)
Category
Date range
📊 Financial Analytics
Total income
Total expenses
Current balance
Category-wise breakdown
Monthly summaries
Recent transactions
👤 Role-Based Access Control
Viewer → View transactions
Analyst → View + access analytics
Admin → Full access (CRUD + user management)
⚠️ Validation & Error Handling
Input validation using Pydantic
Proper HTTP status codes:
400 → Bad request
401 → Unauthorized
403 → Forbidden
404 → Not found
422 → Validation error
🗄️ Database
SQLite database (finance.db)
SQLAlchemy ORM
Auto table creation on startup
📚 API Documentation
Interactive Swagger UI available at:
http://127.0.0.1:8000/docs
🧱 Tech Stack
Component	Technology
Backend	FastAPI
Language	Python 3.11
ORM	SQLAlchemy
Validation	Pydantic
Database	SQLite
Server	Uvicorn
📂 Project Structure
finance_tracker/
│
├── app/
│   ├── main.py              # Entry point
│   ├── database.py         # DB connection
│   ├── models.py           # Database models
│   ├── schemas.py          # Pydantic schemas
│   ├── dependencies.py     # Role & DB dependencies
│   │
│   ├── routers/            # API routes
│   │   ├── transactions.py
│   │   ├── users.py
│   │   └── summary.py
│   │
│   ├── services/           # Business logic
│   │   ├── transaction_service.py
│   │   └── analytics_service.py
│   │
│   └── utils/              # Helpers
│       └── validators.py
│
├── requirements.txt
└── README.md
⚙️ Setup Instructions
1. Clone Repository
git clone <your-repo-link>
cd finance_tracker
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Run Server
uvicorn app.main:app --reload
5. Open API Docs
http://127.0.0.1:8000/docs
🔐 Role Handling

Roles are passed via request headers:

X-Role: admin | analyst | viewer

Optional:

X-User-Id: <user_id>
📌 API Endpoints
🔹 Health
GET /
🔹 Users (Admin)
POST /users
GET /users
GET /users/{user_id}
🔹 Transactions
POST /transactions (Admin)
GET /transactions (Viewer+)
GET /transactions/{id} (Viewer+)
PUT /transactions/{id} (Admin)
DELETE /transactions/{id} (Admin)
🔹 Summary (Analyst+)
GET /summary/overview
GET /summary/category-wise
GET /summary/monthly
GET /summary/recent
📊 Data Models
User
id
name
email (unique)
role
created_at
Transaction
id
user_id
amount
type (income / expense)
category
date
notes
created_at
updated_at
🧠 Assumptions
Single currency system
Simplified authentication using headers
Local database for quick setup and evaluation
✅ Verification
Application starts successfully
API endpoints are functional
Swagger UI available for testing
🚀 Future Enhancements
JWT Authentication
Pagination & search
Unit and integration tests
CSV/JSON import-export
Docker deployment
📄 License

This project is created for educational and assessment purposes.

🙌 Author

Shreyans M
