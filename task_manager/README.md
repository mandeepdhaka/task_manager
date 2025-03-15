# Task Management API

## Setup Instructions

1. Clone the repository or unzip the zip folder(if not using git repository).
2. Set up a virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`

## API Endpoints

- **POST /api/v1/user/ register/**: Register a new user.
- **POST /api/v1/user/login/**: Log in the registered user .
- **GET /api/v1/tasks/**: List all tasks. Can filter by `status` query parameter (e.g., `?status=pending`).
- **POST /api/v1/tasks/**: Create a new task.
- **PUT /api/v1/tasks/{id}/**: Update an existing task.
- **DELETE /api/v1/tasks/{id}/**: Delete a task.
- **POST /api/v1/tasks/{id}/mark_completed/**: Mark a task as completed (simulates Lambda notification).
