import requests
import json

def execute_code(code):
    url = "https://emkc.org/api/v2/piston"

    data = {
        "language": "python3",  
        "version": "3.8",       
        "files": [
            {
                "name": "main.py",        
                "content": '''print("Hello, World!")'''  
            }
        ],
        "stdin": "",  
        "args": [],    
        "run_timeout": 5000,  
        "compile_timeout": 5000,  
        "run_memory_limit": 104857600  
    }

    response = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

    if response.status_code == 200:
        result = response.json()
        print("Output:\n", result["run"]["stdout"])  
        if "stderr" in result["run"]:
            print("Error:\n", result["run"]["stderr"])  
    else:
        print(f"Error: {response.status_code}, {response.text}")


execute_code("print('Hello, World!')")  