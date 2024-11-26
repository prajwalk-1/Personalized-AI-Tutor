import os
from dotenv import load_dotenv

load_dotenv()

# Configuration settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# EMBEDDING_MODEL = "text-embedding-ada-002"

if OPENAI_API_KEY is None:
    raise ValueError("OpenAI API key not found. Please add it to the .env file.")
