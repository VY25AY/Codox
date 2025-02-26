# Codox - Intelligent IDE

The Codox - Intelligent IDE is an AI-powered integrated development environment designed to enhance developer productivity by automating key aspects of the software development lifecycle. It includes features such as automated code generation, test generation, and AI-driven debugging.

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
     ```json
     { "language": "java", "code": "public class Main { public static void main(String[] args) { int number = 6; long result = factorial(number); System.out.println(\"Factorial of \" + number + \" is: \" + result); } public static long factorial(int n) { long result = 1; for (int i = 1; i <= n; i++) { result *= i; } return result; }}" }
     ```

   - Sample Response:
     ```json
     { "result": "Factorial of 6 is: 720" }
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

### Setting up the backend
Make sure you have Python 3.9 or later installed.

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