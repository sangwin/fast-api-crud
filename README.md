# FastAPI User CRUD Application

A simple **User CRUD (Create, Read, Update, Delete) REST API** built using **FastAPI**.  
This project is designed for learning FastAPI fundamentals with clean code structure and best practices.

---

## 🚀 Features

- Create a new user
- Fetch all users
- Fetch user by ID
- Update user details
- Delete a user
- Auto-generated API documentation (Swagger UI)
- Preloaded demo users for initial fetch
- Clean, modular project structure

---

## 🛠 Tech Stack

- **Python**
- **FastAPI**
- **Uvicorn**
- **Pydantic**

---

## 📁 Project Structure

```
fastapi-crud/
│
├── app/
│   ├── main.py          # Application entry point
│   ├── routes.py        # API routes (CRUD operations)
│   ├── models.py        # Pydantic data models
│   ├── database.py     # In-memory database with demo users
│   └── __init__.py
│
├── requirements.txt
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

| Method | Endpoint           | Description            |
|------|-------------------|------------------------|
| POST | `/users`          | Create a new user      |
| GET  | `/users`          | Get all users          |
| GET  | `/users/{id}`     | Get user by ID         |
| PUT  | `/users/{id}`     | Update user            |
| DELETE | `/users/{id}`   | Delete user            |

---

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
