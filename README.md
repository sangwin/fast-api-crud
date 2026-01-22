# FastAPI User CRUD Application

A simple **User CRUD (Create, Read, Update, Delete) REST API** built using **FastAPI**.  
This project is designed for learning FastAPI fundamentals with clean code structure and best practices.

---

## 🚀 Features

- User CRUD operations (Create, Read)
- JWT-based Authentication (OAuth2 Password Flow)
- Password hashing using **Argon2**
- Protected routes using dependency injection
- Centralized error handling
- Custom middleware for API timing
- Structured **JSON logging** (console + file)
- Auto-generated API documentation (Swagger & ReDoc)
- Clean, scalable folder structure

---

## 🛠 Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- Passlib (Argon2)
- Python-JOSE (JWT)

---

## 📁 Project Structure

```
fastapi-crud/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── auth.py
│   ├── middleware.py
│   ├── logger.py
│   ├── error_handler.py
│   ├── routers/
│   │   ├── auth.py
│   │   └── users.py
│   └── __init__.py
├── logs/
├── requirements.txt
├── .gitignore
└── README.md
```

---


## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone <repository-url>
cd fastapi-crud
```

### 2️⃣ Create virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

From the **project root directory**, run:

```bash
uvicorn app.main:app --reload
```

Server will start at:
```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI provides automatic interactive API docs:

- **Swagger UI:**  
  👉 http://127.0.0.1:8000/docs

- **ReDoc:**  
  👉 http://127.0.0.1:8000/redoc

---

## 📌 Sample Endpoints

| Method | Endpoint      | Description           | Auth |
| ------ | ------------- | --------------------- | ---- |
| POST   | `/login`      | Login & get JWT token | ❌    |
| POST   | `/users`      | Create user           | ❌    |
| GET    | `/users`      | Get all users         | ✅    |
| GET    | `/users/{id}` | Get user by ID        | ✅    |

---
## 📊 Logging

Logs are written in JSON format

Logged to:

Console

logs/api_timing.log

Includes:

HTTP method

Path

Status code

Start time

End time

Duration (ms)

------

## 🛡 Error Handling

Centralized exception handlers

Consistent JSON error responses

No sensitive stack traces exposed

Validation, auth, and server errors handled

------

## 🔮 Future Enhancements

Database integration (PostgreSQL / SQLite)

Async SQLAlchemy ORM

Role-based access control (RBAC)

Refresh tokens

Rate limiting

Docker & CI/CD support
--

## 🧪 Demo Data

The application loads **demo users automatically** on startup for easy testing.

---

## 🔮 Future Enhancements

- SQLite / PostgreSQL integration
- SQLAlchemy ORM
- Authentication (JWT)
- Pagination & filtering
- Unit tests with Pytest
- Docker support

---

## 👨‍💻 Author

**Sangwin Gawande**  
https://samgw.in

Full Stack Developer  
- 11+ years of experience in Frontend & Backend development  
- Expertise in Angular, JavaScript, TypeScript, Python, FastAPI, and SaaS applications  
- Passionate about clean architecture, scalable systems, and developer education  

---

## 📄 License

This project is for **learning and educational purposes**.
