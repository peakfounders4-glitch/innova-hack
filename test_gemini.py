import time
import os
from dotenv import load_dotenv

print("Sleeping 18 seconds to clear any 429 rate limit cooldown...")
time.sleep(18)

load_dotenv()

models_to_test = [
    'gemini-2.0-flash',
    'gemini-3.1-flash-lite',
    'gemini-3-pro-preview'
]

from google.genai import Client
client = Client()

for model_name in models_to_test:
    print(f"--- Testing {model_name} ---")
    try:
        response = client.models.generate_content(
            model=model_name,
            contents='Hello, say hi!'
        )
        print(f"SUCCESS: {model_name} response: {response.text}")
    except Exception as e:
        print(f"FAILED: {model_name} error: {e}")
