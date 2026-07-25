import os
from dotenv import load_dotenv, find_dotenv

# Use find_dotenv(usecwd=True) to locate the .env file in CWD
load_dotenv(find_dotenv(usecwd=True))

print("Loaded GEMINI_API_KEY:", repr(os.environ.get("GEMINI_API_KEY")))
