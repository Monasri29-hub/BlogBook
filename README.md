# 📖 BlogBook

A simple blog application built with **Django**.  
This project allows users to sign up, log in, create posts, view their own posts, and manage sessions with authentication.

---

## 🚀 Features
- User authentication (signup, login, logout)
- Create new blog posts
- View all posts on the home page
- Profile dropdown with quick actions:
  - New Post
  - My Posts
  - Sign Out
- Responsive UI with Bootstrap

---

## 🛠️ Tech Stack
- **Backend**: Django 5.2
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default Django database)
- **Version Control**: Git & GitHub

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Monasri29-hub/BlogBook.git
   cd BlogBook
2. **- Create a virtual environment**
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
3. **- Install dependencies**
   pip install -r requirements.txt
4. **- Apply migrations**
   python manage.py migrate
5. **Run the development server**
   python manage.py runserver
6. **Open your browser and go to:**
    http://127.0.0.1:8000/
