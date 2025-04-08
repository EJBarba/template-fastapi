# 🚀 FastAPI Project Template

A clean and scalable starting point for building **FastAPI** applications using **SQLAlchemy** and **Alembic** for database management.

---

## 🧰 Features

- 🔧 FastAPI framework for high-performance APIs  
- 🗄️ SQLAlchemy ORM for database interactions  
- 🔄 Alembic for handling migrations  
- 🔐 Environment-based configuration via `.env`  
- 🧪 Ready for expansion with Pydantic models, routers, and services  

---

## 📦 Getting Started

Follow these steps to get your project up and running:

### 1. Clone or Copy the Template

Copy the `new_fastapi_project/` directory to your desired location and rename it:

```bash
cp -r new_fastapi_project my_project
cd my_project
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file using `.env.example` as a reference:

```bash
cp .env.example .env
```

Edit the `.env` file with your configuration:

```env
DATABASE_URL=postgresql://user:password@host:port/database_name
# Optional: API_KEY=your_secret_key
```

📌 **Need help generating an API key?**  
[How to generate API Key in Python](https://chatgpt.com/share/67f4b34c-ae38-800e-a327-e7874c1e46d1)

---

### 5. Set Up Alembic

#### Initialize Alembic (if not already initialized):

```bash
alembic init alembic
```

#### Configure Alembic:

- In `alembic.ini`, set `sqlalchemy.url` or load it from the `.env`.
- In `alembic/env.py`, import `Base` from your `app.database` and assign it to `target_metadata`.

---

### 6. Run Database Migrations

#### Apply existing migrations:

```bash
alembic upgrade head
```

#### Create new migrations after model changes:

```bash
alembic revision --autogenerate -m "Your migration message"
alembic upgrade head
```

---

### 7. Start the Development Server

```bash
uvicorn app.main:app --reload
```

---

## 🗂️ Project Structure

```
new_fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app entry point
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   └── database.py      # DB connection and session management
├── alembic/
│   ├── env.py
│   ├── README
│   └── versions/        # Auto-generated migration scripts
├── .env.example         # Sample env file
├── requirements.txt     # Dependencies
└── README.md            # Project overview
```

---

## 🛠️ Next Steps

- ✅ **Define Models** in `app/models.py`  
- ✅ **Create Schemas** in `app/schemas.py`  
- ✅ **Build Routes** in `app/main.py` or split with FastAPI routers  
- ✅ **Write Services** and business logic in separate modules  
- ✅ **Test your endpoints** using tools like [httpie](https://httpie.io/), [Postman](https://www.postman.com/), or Swagger UI  

---

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)  
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)  
- [Alembic Docs](https://alembic.sqlalchemy.org/)  
- [Pydantic Docs](https://docs.pydantic.dev/)
