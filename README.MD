# Project Setup Guide

This guide will help you set up and run the project locally.



### 1. Firebase Configuration
You'll need a `key.json` file in the root directory for Cloud Firestore access:
1. Create a new Firebase database
2. Generate and download the service account key
3. Rename it to `key.json` and place it in the project root

### 2. Environment Configuration
Create a `.env` file in the root directory with your Gemini API key:
```env
GEMINI_API_KEY=your_api_key_here
```
> You can obtain a free Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### 3. Python Setup

#### Create Virtual Environment
```bash
# Create a new virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Running the Application
```bash
python main.py
```

## Project Structure
```
├── .venv/
├── src/
│   ├── menu_service.py
│   └── ....
├── prompts/
│   ├── breakDownInformation.txt
│   └── ....
├── main.py
├── requirements.txt
├── key.json
├── .gitignore
└── .env
```

## Support
If you encounter any issues or have questions, please open an issue in the repository.