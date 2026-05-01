# Task Manager API - Backend 

## Project Overview
This project is a scalable REST API built with **FastAPI** and **SQLAlchemy**, featuring secure JWT-based authentication and Role-Based Access Control (RBAC)[cite: 5, 11]. It includes a persistent SQLite database and a functional Vanilla JS frontend to demonstrate seamless API integration.

---

## Core Features
* **Secure Authentication**: User registration and login with `bcrypt` password hashing and JWT token generation.
* **Role-Based Access Control (RBAC)**: 
    * **User**: Can create tasks and view only their own tasks.
    * **Admin**: Can view all tasks across the entire system.
* **CRUD Operations**: Full Create and Read functionality for the "Tasks" entity.
* **Persistent Database**: Integrated SQLite with SQLAlchemy ORM for schema management.
* **API Documentation**: Automatic interactive documentation via Swagger UI.
* **Frontend UI**: A clean, responsive dashboard for interacting with the API in real-time.

---
## Installation
git clone https://github.com/Ramnik2003/Scalable-REST-API.git
pip install -r requirements.txt
python -m app.main
Run live - index.html

## Frontend Running


