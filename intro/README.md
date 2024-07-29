# Intro example

Set up virtual environment:

```bash
virtualenv ../.venv
source ../.venv/bin/activate
```

Install FastAPI:

```bash
pip install fastapi
```

Run the code:

```bash
fastapi dev main.py
```

Available endpoints:

1. Intro: <http://127.0.0.1:8000>
2. JSON Query: <http://127.0.0.1:8000/items/5?q=somequery>
3. Interactive API docs: <http://127.0.0.1:8000/docs>
4. Alternative API docs: <http://127.0.0.1:8000/redoc>