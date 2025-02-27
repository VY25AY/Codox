import requests
import json
from constants import LANGUAGE_VERSIONS
from config import config

Piston_URL = config.get('Piston_URL')
url = f'{Piston_URL}/execute'


def execute_code(code, language, stdinput=""):

    json_data = {
        "language": language,
        "version": LANGUAGE_VERSIONS[language],
        "files": [
            {
                "content": code
            }
        ],
        "stdin": stdinput,
        "run_memory_limit": 104857600
    }

    response = requests.post(url=url, data=json.dumps(json_data), headers={
        "Content-Type": "application/json"
    })

    return response.json()
