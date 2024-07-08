# ToDo-DRF

This is a ToDo application built using React for the frontend, Django Rest Framework (DRF) for the backend, and MySQL for the database.



## Features

- Create, read, update, and delete todo items
- Mark todos as complete/incomplete
- Filter todos by status (all, active, completed)
- User authentication and authorization
- Responsive design for mobile and desktop

## Tech Stack

- Frontend: React
- Backend: Django REST Framework
- Database: MySQL
- API: RESTful

## Prerequisites

- Node.js (v14+)
- Python (v3.8+)
- MySQL

  ## Installation


cd ToDoApp
python -m venv env
source env/bin/activate  # On Windows use env\Scripts\activate
pip install -r requirements.txt

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
2. Backend Setup (Django REST Framework)
   cd ToDoApp
python -m venv env
source env/bin/activate  # On Windows use env\Scripts\activate
pip install -r requirements.txt
4. Configure the database:
- Create a MySQL database
- Update `backend/settings.py` with your database credentials
4.Set up MySQL database:

Create a MySQL database and note down the credentials.
Update the database settings in backend/settings.py.
Run database migrations:
python manage.py makemigrations
python manage.py migrate

Start the Django development server:
python manage.py runserver

#Frontend Setup (React)

Open a new terminal window/tab.

Navigate to the frontend directory:
npm install
npm start

###Usage

Access the application through the provided URLs for the frontend and backend.
Use the To-Do application to manage your tasks by adding, editing, completing, and deleting them.

#Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
