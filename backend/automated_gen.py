from google import genai
from config import config

Gemini_Api_key = config.get('Gemini_Api_key')


def generate_code(prompt):
    client = genai.Client(api_key=Gemini_Api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f'Generate code for {prompt}. do not provide any suggestions. I only want code.'
    )
    return response.text
