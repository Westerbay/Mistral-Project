@echo off
if not exist venv (
    echo [INFO] Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

echo [INFO] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo [INFO] Starting the application...
python backend\__main__.py

pause
