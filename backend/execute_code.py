import requests
import json
from constants import LANGUAGE_VERSIONS


def execute_code(code, language, stdinput):
    url = "https://emkc.org/api/v2/piston"

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

    response = requests.post(f'{url}/execute', data=json.dumps(json_data), headers={
        "Content-Type": "application/json"
    })

    return response.json()
