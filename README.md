# Codox - Intelligent IDE

The Codox - Intelligent IDE is an AI-powered integrated development environment designed to enhance developer productivity by automating key aspects of the software development lifecycle. It includes features such as automated code generation, test generation, and AI-driven debugging.

## Demo


## Key Features

- **Automated Code Generation**: AI-powered code completion and snippet generation.
- **Automated Test Creation**: AI-driven test case generation and edge case identification.
- **AI-Driven Debugging**: Real-time code analysis and automated bug fixes.
- **Multi-Language Support**: Supports Java, Python, C++, JavaScript, and TypeScript.

## Future Enhancements:

- Peer-to-peer collaboration.
- User authentication and role-based access control.
- Built-in coding challenges and AI-driven optimizations.

## Technologies Used

### Backend

- Python3
- Dotenv
- FastAPI
- Gemini API
- Piston API

### Frontend

- React.js
- Tailwind CSS
- Chakra UI
- Monaco Editor
- Axios

## Endpoints

### Backend

1. **Generate Code** (`POST /generate-code/`)

   - Sample Request:

     ```json
     { "prompt": "Write a Python function to reverse a string." }
     ```

   - Sample Response:
     ```json
     { "generated_code": "def reverse_string(s): return s[::-1]" }
     ```

2. **Run Code** (`POST /run-code/`)

   - Sample Request:

     ````json
     {
       "language": "java",
       "code": "```java\npublic class Factorial {\n\n    public static void main(String[] args) {\n        int number = 5; // You can change this number to calculate the factorial of a different number\n        long factorial = calculateFactorial(number);\n        System.out.println(\"Factorial of \" + number + \" = \" + factorial);\n    }\n\n    public static long calculateFactorial(int n) {\n        if (n == 0) {\n            return 1;\n        } else {\n            return n * calculateFactorial(n - 1);\n        }\n    }\n}\n```\n",
       "stdinput": ""
     }
     ````

   - Sample Response:
     ```json
     { "result": "Factorial of 5 is: 120" }
     ```

### Frontend

1. `/` - Home page with the main code editor.
2. `/debug/` - Debugging page with step-by-step execution controls.

## Impact

- **Increased Developer Productivity**: Automates repetitive tasks, enabling focus on problem-solving.
- **Improved Code Quality**: AI-powered analysis reduces errors and enhances maintainability.
- **Reduced Operational Costs**: Automation lowers debugging, testing, and integration efforts.
- **Enhanced Collaboration**: AI-generated documentation and standardized practices improve teamwork.
- **Future-Proofing**: Adaptable to modern cloud-based development.

## Setting up the project:

1. Clone the github repository

   ```bash
   git clone https://github.com/VY25AY/Codox.git
   ```

2. Open the project directory

   ```bash
   cd Codox
   ```

3. Set up the Backend and Frontend

### Setting up the backend

Make sure you have Python or later installed.

1. Open backend directory:

   ```bash
   cd backend
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:

   - For Linux/Mac:

     ```bash
     source .venv/bin/activate
     ```

   - For Windows:

     ```bash
     .\.venv\Scripts\activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the backend server:

   ```bash
   uvicorn main:app --reload
   ```

6. Backend server is now running on http://localhost:8000.

### Setting up the Frontend

Make sure you have Node.js installed.

1. Open frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the frontend server:

   ```bash
   npm start
   ```

4. The frontend will be running on http://localhost:5173.

## Usage

1. Open your web browser.

2. Go to this URL: http://localhost:5173.
