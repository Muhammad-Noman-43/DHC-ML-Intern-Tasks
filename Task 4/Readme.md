# Medical Assistant Chatbot

A friendly and helpful medical assistant chatbot powered by the **Mistral-7B** language model. This chatbot provides simple explanations for medical problems, suggests possible causes, and recommends consulting a licensed doctor for serious concerns.

## Features

- Interactive medical assistance via **command-line interface**
- Safe prompt filtering to prevent harmful requests
- Easy-to-read formatted output using **rich** terminal styling
- Powered by **Mistral-7B** model through **Hugging Face API**
- System prompts designed to provide helpful, non-diagnostic medical information

## Project Setup

### 1. Virtual Environment

It is recommended to create a virtual environment for this project to keep dependencies isolated:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate
```

### 2. Install Dependencies

With the virtual environment activated, install the required packages:

```bash
pip install huggingface_hub requests rich python-dotenv
```

**Dependencies:**

- **huggingface_hub**: For connecting to Hugging Face
- **requests**: For making HTTP requests to the Hugging Face API
- **rich**: For formatting and displaying text beautifully in the terminal
- **python-dotenv**: For loading environment variables from a `.env` file

### 3. Environment Variables (.env File)

Create a `.env` file in the project root directory to store your Hugging Face API token:

```
HF_TOKEN = your_huggingface_token_here
```

**Important:** The `.env` file is **not uploaded** to the repository for security reasons. You must create this file locally with your own Hugging Face API token.

## Usage

Run the chatbot:

```bash
python chatbot.py
```

Enter your medical question via **command-line** when prompted, and the chatbot will provide a friendly, simplified response along with suggestions to consult a licensed doctor for serious concerns.

## Technical Details

- **Rich Library**: Used solely for formatting markdown output in the terminal to improve readability
- **Safety Filter**: Blocks requests containing dangerous keywords to prevent harmful usage
- **System Prompt**: Instructs the model to provide simple explanations, suggest causes/solutions, and always recommend consulting a licensed doctor

## Notes

- This is an educational/internship project
- The chatbot is designed to provide general information only, not medical advice
