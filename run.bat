@echo off

if not exist venv (
    echo [INFO] Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

setlocal enabledelayedexpansion
if not exist .env (
    echo [INFO] .env file not found, creating one...

    set /p API_KEY="Enter your Mistral API key: "
    set /p MODEL="Enter the Mistral model (default: mistral-large-latest): "

    if "!MODEL!"=="" (
        set MODEL=mistral-large-latest
    )

    (
        echo MISTRAL_API_KEY=!API_KEY!
        echo MISTRAL_MODEL=!MODEL!
    ) > .env

    echo [INFO] .env file created
)
endlocal

echo [INFO] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo [INFO] Running tests...
pytest -v backend/test.py

echo [INFO] Starting the application...
python backend\__main__.py

pause
