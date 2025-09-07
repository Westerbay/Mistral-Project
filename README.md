# Mistral Chatbot with FastAPI

This project is a **chatbot application** powered by [Mistral AI](https://docs.mistral.ai/) and built with [FastAPI](https://fastapi.tiangolo.com/).  
It provides multiple modes of interaction, from a classic AI assistant to code analysis, summarization, translation, and quiz generation.  

---

## Features

You can choose between **five chatbot modes** when starting the application:

1. **AIModel (Classic Bot)**  
   - A general-purpose chatbot for casual conversation or answering questions.

2. **AIDevHelper**  
   - An assistant for developers.  
   - Explains code step by step, suggests optimizations, and even generates unit tests.

3. **AIQuiz**  
   - Creates a quiz on a chosen topic to help with learning or practice.

4. **AISummarize**  
   - Summarizes long texts into essential points.

5. **AITranslate**  
   - Translates text automatically into a chosen foreign language.

When you select a mode, the application will display a short explanation of its functionality.

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/Westerbay/Mistral-Project
```

### 2. Configure environment variables
Create a `.env` file in the project root with the following content:

```env
MISTRAL_API_KEY=your_api_key
MISTRAL_MODEL=mistral-large-latest
```

- Replace `your_api_key` with your Mistral API key.  
- `MISTRAL_MODEL` defaults to `mistral-large-latest`, but you can use another supported model.

---

## Running the application

### On **Windows**
Run the batch script:
```bash
run.bat
```

### On **Linux/macOS**
Run the shell script:
```bash
chmod +x run.sh
./run.sh
```

---

## What the script does

1. Creates (if missing) and activates a **Python virtual environment**.
2. Creates (if missing) `.env` file
3. Installs dependencies from `requirements.txt`.
4. Runs unit tests with `pytest`.
5. Starts the FastAPI server on **http://localhost:8000**.

---

## Using the chatbot

Once the server is running, open your browser and go to: [http://localhost:8000](http://localhost:8000)

From there, you can select the chatbot mode you want to use.

