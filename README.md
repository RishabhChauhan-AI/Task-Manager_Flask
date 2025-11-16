# Task Manager Flask App

A simple yet functional Task Manager application built with **Flask**, featuring:

- User registration & login
- Secure password hashing 
- Task creation, deletion, and status toggling
- Persistent data using SQLite and SQLAlchemy
- Basic CSS styling with Bootstrap

---

## 🚀 Features

- **Register** a new user
- **Login** and manage sessions securely with `Flask-Login`
- **Add, toggle, and delete tasks**
- Each task has a status: `pending`, `working`, or `done`
- Protected routes ensure only logged-in users can access task management

---

## 🛠️ Tech Stack

- Backend: **Flask**
- Database: **SQLite + SQLAlchemy**
- User Auth: **Flask-Login **
- Frontend: **HTML + Jinja2 + CSS (Bootstrap)**
- Version Control: **Git + GitHub**

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/RishabhChauhan-AI/Task-Manager_Flask.git
cd Task-Manager_Flask
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the App
```bash
python run.py
```
### 3. Visit in Browser
```bash
http://127.0.0.1:5000/auth/login
```
