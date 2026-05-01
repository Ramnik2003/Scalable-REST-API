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
* git clone https://github.com/Ramnik2003/Scalable-REST-API.git
* pip install -r requirements.txt
* python -m app.main
* Run live - index.html

## Frontend Running
* When index.html is live the webpage appears:
  <img width="1909" height="705" alt="image" src="https://github.com/user-attachments/assets/b81bdcc4-09bb-4658-b1c8-628d6d74b037" />
* New User can register:
  <img width="352" height="242" alt="image" src="https://github.com/user-attachments/assets/0cf3e0c2-ddbe-4ebc-a3f2-0226304b3425" />
* New user can login:
  <img width="705" height="424" alt="image" src="https://github.com/user-attachments/assets/10546237-0952-44d0-8fc7-8b033279c703" />
* User can add task to be completed:
  <img width="667" height="552" alt="image" src="https://github.com/user-attachments/assets/f148dc20-37dc-4494-add5-cf846dc2ae6f" />
* New task will be listed under tasks list:
  <img width="641" height="605" alt="image" src="https://github.com/user-attachments/assets/97fb1447-0ec3-47d6-9f55-b4b4d86ea96a" />
* If admin logs in then he can see all user tasks + admin tasks:

  <img width="626" height="764" alt="image" src="https://github.com/user-attachments/assets/1a20c006-b43b-46c4-9ea8-0cab661105d9" />

---
## Swagger UI
<img width="1890" height="937" alt="image" src="https://github.com/user-attachments/assets/d6f5e42a-72c3-4039-8e6a-df3349498552" />








