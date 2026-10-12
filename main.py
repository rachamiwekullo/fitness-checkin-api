"""FastAPI backend for a small in-memory daily fitness check-in demo."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, ConfigDict, Field

STATIC_DIR = Path(__file__).with_name("static")
app = FastAPI(title="Fitness Check-in API", version="1.0.0")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
checkins: list[dict[str, object]] = []


class CheckInInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(min_length=1, max_length=50)
    sleep: float = Field(ge=0, le=24)
    water: int = Field(ge=0, le=30)
    steps: int = Field(ge=0, le=100_000)


@app.get("/", include_in_schema=False)
def home() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/checkins")
def get_checkins() -> list[dict[str, object]]:
    return checkins


@app.post("/api/checkins", status_code=201)
def add_checkin(data: CheckInInput) -> dict[str, object]:
    entry: dict[str, object] = data.model_dump()
    entry["hit_goal"] = data.steps >= 10_000
    entry["id"] = len(checkins) + 1
    checkins.append(entry)
    return {"success": True, "stored": entry}

