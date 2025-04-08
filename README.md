
# FastAPI Project Template

  

A streamlined starting point for building FastAPI applications with SQLAlchemy and Alembic for database management.

  

## Getting Started

  

Follow these steps to set up your new project:

  

1.  **Copy the template:** Duplicate the `new_fastapi_project` directory to your desired project location.

2.  **Rename the directory:** Give your project directory a new, descriptive name.

3.  **Set up the environment:**

```bash

python -m venv venv

source venv/bin/activate # macOS/Linux

venv\Scripts\activate # Windows

pip install -r requirements.txt

```

4.  **Configure environment variables:** Create a `.env` file based on `.env.example` and populate it with your database URL.

5.  **Initialize Alembic:**

```bash

alembic init alembic

```

6.  **Configure Alembic:**

- Edit `alembic.ini` to update `sqlalchemy.url` with your database connection string (you can access environment variables here if needed).

- Verify that `target_metadata` in `alembic/env.py` correctly imports `Base` from your `app.database` module.

7.  **Run initial migrations:**

```bash

alembic upgrade head

```

8.  **Start the development server:**

```bash

uvicorn app.main:app --reload

```

  

## Project Structure

  

Markdown

  

# FastAPI Project Template

  

A streamlined starting point for building FastAPI applications with SQLAlchemy and Alembic for database management.

  

## Getting Started

  

Follow these steps to set up your new project:

  

1.  **Copy the template:** Duplicate the `new_fastapi_project` directory to your desired project location.

2.  **Rename the directory:** Give your project directory a new, descriptive name.

3.  **Set up the environment:**

```bash

python -m venv venv

source venv/bin/activate # macOS/Linux

venv\Scripts\activate # Windows

pip install -r requirements.txt

```

4.  **Configure environment variables:** Create a `.env` file based on `.env.example` and populate it with your database URL.

5.  **Initialize Alembic:**

```bash

alembic init alembic

```

6.  **Configure Alembic:**

- Edit `alembic.ini` to update `sqlalchemy.url` with your database connection string (you can access environment variables here if needed).

- Verify that `target_metadata` in `alembic/env.py` correctly imports `Base` from your `app.database` module.

7.  **Run initial migrations:**

```bash

alembic upgrade head

```

8.  **Start the development server:**

```bash

uvicorn app.main:app --reload

```

  

## Project Structure

  
```
new_fastapi_project/

├── app/

│ ├── init.py

│ ├── main.py # FastAPI application entry point

│ ├── models.py # SQLAlchemy database models

│ ├── schemas.py # Pydantic data validation schemas

│ └── database.py # Database connection and setup

├── alembic/

│ ├── env.py # Alembic environment configuration

│ ├── README

│ └── versions/ # Database migration scripts

├── .env.example # Example environment variable file

├── requirements.txt # Project dependencies

└── README.md # Project overview and setup instructions
```
  

## Next Steps

  

-  **Define Models:** Create your database tables as SQLAlchemy models in `app/models.py`.

-  **Create Schemas:** Define Pydantic schemas for data validation and serialization in `app/schemas.py`.

-  **Build API Endpoints:** Implement your API routes and logic within `app/main.py`. Consider using routers for better organization in larger projects.

-  **Generate Migrations:** When you modify your models, create Alembic migration scripts to update your database schema:

```bash

alembic revision --autogenerate -m "Describe your changes"

```

-  **Apply Migrations:** Execute the generated migration scripts to update your database:

```bash

alembic upgrade head

```
