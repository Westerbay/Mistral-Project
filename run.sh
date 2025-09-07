#!/usr/bin/bash
set -e 

if [ ! -d "venv" ]; then
    echo "[INFO] Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

if [ ! -f ".env" ]; then
    echo "[INFO] .env file not found, creating one..."

    read -rp "Enter your Mistral API key: " API_KEY
    read -rp "Enter the Mistral model (default: mistral-large-latest): " MODEL

    if [ -z "$MODEL" ]; then
        MODEL="mistral-large-latest"
    fi

    cat > .env <<EOF
MISTRAL_API_KEY=$API_KEY
MISTRAL_MODEL=$MODEL
EOF

    echo "[INFO] .env file created"
fi

echo "[INFO] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[INFO] Running tests..."
pytest -v backend/test.py

echo "[INFO] Starting the application..."
python backend/__main__.py
