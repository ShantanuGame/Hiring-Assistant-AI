import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in .env file!")

def query_llm(prompt: str) -> str:
    """
    Send a prompt to OpenRouter GPT model and return the response.
    """
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openai/gpt-4o-mini-search-preview",
        "messages": [
            {"role": "system", "content": "You are a helpful AI hiring assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raises an exception for 4xx/5xx responses
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except (KeyError, IndexError):
        return f"Unexpected response format: {response.text}"

# Example usage
if __name__ == "__main__":
    print(query_llm("Hello, test if GPT-4o-mini Search Preview is working!"))
