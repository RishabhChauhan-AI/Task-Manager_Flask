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

## 📂 Project Structure
taskmanager/
├── app/
│ ├── templates/
│ │ ├── base.html
│ │ ├── login.html
│ │ ├── register.html
│ │ └── tasks.html
│ ├── static/
│ │ ├── css/
│ │ │ └── style.css
│ │ └── js/
│ │ └── scripts.js
│ ├── routes/
│ │ ├── auth.py
│ │ └── tasks.py
│ ├── models.py
│ └── init.py
├── run.py
├── requirements.txt
└── .gitignore

