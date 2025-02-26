import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "Gemini_Api_key": os.getenv("Gemini_Api_key"),
    "Frontend_URL": os.getenv("Frontend_URL"),
    "Piston_URL": os.getenv("Piston_URL"),
}
