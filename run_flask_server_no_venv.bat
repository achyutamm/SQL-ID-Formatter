@echo off
REM Change to the directory where your Flask app is located
cd /d "C:\Python\SQL ID Formatter\app.py"

REM Activate the virtual environment
call venv\Scripts\activate

REM Set Flask environment variables
set FLASK_APP=app.py
set FLASK_ENV=development

REM Run the Flask server
flask run

REM Deactivate the virtual environment after the server stops
deactivate
pause
