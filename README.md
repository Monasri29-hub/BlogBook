# 📖 BlogBook

A simple blog application built with **Django**.  
This project allows users to sign up, log in, create posts, view their own posts, and manage sessions with authentication.

<img width="1906" height="1008" alt="image" src="https://github.com/user-attachments/assets/6e43f1ba-a794-45b5-b3c0-db0fdfb62264" />


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
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Apply migrations**
   ```bash
    python manage.py migrate
5. **Run the development server**
   ```bash
   python manage.py runserver
6. **Open your browser and go to:**
    ```bash
    http://127.0.0.1:8000/
