@echo off
echo Starting Backend...
start cmd /k "cd backend && venv\Scripts\activate && python manage.py runserver"

echo Starting Frontend...
start cmd /k "cd frontend && npm run dev"

echo Both servers are starting in separate windows. You can access the site at http://localhost:5173
