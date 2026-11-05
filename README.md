# Local Fruit Atlas

A small FastAPI app that serves a responsive fruit guide and its stylesheet from the same local server.

## Run on Windows

1. Open a terminal in this folder.
2. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies and start the development server:

   ```powershell
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

4. Open http://127.0.0.1:8000.

The page is rendered by FastAPI using the template in `templates/`, and local static files are served from `static/`.
