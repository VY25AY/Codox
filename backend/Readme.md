## Setting up the backend
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

    ```bash
    source .venv/bin/activate  # On Linux/Mac
    .\.venv\Scripts\activate  # On Windows
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