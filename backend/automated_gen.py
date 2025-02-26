from google import genai
from config import config

Gemini_Api_key = config.get('Gemini_Api_key')
def generate_code(prompt):
    client = genai.Client(api_key=Gemini_Api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text


