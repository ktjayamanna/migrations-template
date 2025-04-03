# FastAPI + SQLAlchemy + Alembic + PostgreSQL (in Docker) Template

This project is a template for building a web application using FastAPI, SQLAlchemy, and Alembic for database migrations. It also includes a PostgreSQL database running in a Docker container.

### Features

- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- SQLAlchemy: The SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- Alembic: A lightweight database migration tool for SQLAlchemy.
- PostgreSQL: A powerful, open source object-relational database system.
- Docker: A containerization platform for deploying applications.

### How to use

1. Clone the repository.
2. Install the dependencies with `pip install -r requirements/default.txt`.
3. Run the PostgreSQL database with `docker-compose up -d`.
4. Initialize the database with `alembic upgrade head`.
5. Run the application with `uvicorn bitly.server.write_service.api:app --host 0.0.0.0 --port 8000 --reload`.
6. Open your web browser and navigate to `http://localhost:8000/docs` to access the API documentation.

## Please note that this repository contains code snippets from an external source (https://github.com/ktjayamanna/bitly-system-design-implementation) that should be removed before use.