import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")  # Make sure your .env has this key

def query_llm(prompt):
    """
    Send a prompt to OpenRouter GPT-4o-mini Search Preview model and return the response.
    """
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-4o-mini-search-preview",  # your chosen free model
        "messages": [
            {"role": "system", "content": "You are a helpful AI hiring assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"

# Test the API
if __name__ == "__main__":
    print(query_llm("Hello, test if GPT-4o-mini Search Preview is working!"))
