# Fitness Check-in API

A small full-stack check-in demo. A browser form submits sleep, water, and step
counts to a FastAPI backend, which validates each entry and flags whether the
10,000-step threshold was reached.

## What It Does

- Serves a browser-based daily check-in form
- Validates check-in fields and their allowed ranges
- Accepts and lists check-ins through a JSON API
- Flags entries with at least 10,000 steps
- Provides interactive API documentation

## Setup

Requires Python 3.10 or newer.

```bash
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

## Usage

Open <http://127.0.0.1:8000> to use the form. To submit a check-in directly:

```bash
curl -X POST http://127.0.0.1:8000/api/checkins \
  -H "Content-Type: application/json" \
  -d '{"name":"Sample Member","sleep":8,"water":8,"steps":10500}'
```

List check-ins with `GET http://127.0.0.1:8000/api/checkins`; open
<http://127.0.0.1:8000/docs> for the API explorer. Run tests with
`python -m unittest -v`.

## Sample Output

```json
{
  "success": true,
  "stored": {
    "name": "Sample Member",
    "sleep": 8.0,
    "water": 8,
    "steps": 10500,
    "hit_goal": true,
    "id": 1
  }
}
```

## Stack

Python, FastAPI, Pydantic, Uvicorn, HTML, JavaScript

Records are kept in memory and disappear when the server restarts. This
learning demo is not a health application; do not enter sensitive or real
participant data.
