import os
from dotenv import load_dotenv

load_dotenv()

def get_provider():
    """
    Decide provider from environment variables.
    Priority: GEMINI > OPENAI
    """
    if os.getenv("GEMINI_API_KEY"):
        return "gemini"
    if os.getenv("OPENAI_API_KEY"):
        return "openai"
    return None

