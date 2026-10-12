# Fitness Check-in API

A small FastAPI and browser-JavaScript example. The form submits daily
check-ins, the API validates inputs and flags whether the sample 10,000-step
threshold was reached, and the page lists check-ins returned by the API.

Records are stored only in memory and disappear when the server restarts.
This is a learning demo, not a health application; do not enter sensitive or
real participant data.

## Run

Requires Python 3.10 or newer.

```powershell
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Open <http://127.0.0.1:8000>. The API docs are at
<http://127.0.0.1:8000/docs>.

```powershell
python -m unittest -v
```

## Project source

Based on the Python API and JavaScript integration exercise in Week 8, Day 4.
