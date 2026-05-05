from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from .client import DramaBoxClient


class SearchPayload(BaseModel):
    keyword: str
    page: int = Field(default=1, ge=1)
    size: int = Field(default=20, ge=1, le=100)


class ListPayload(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=20, ge=1, le=100)


app = FastAPI(title="DramaBox Scraper API", version="2.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_DIST = Path("frontend/dist")
if _DIST.exists():
    app.mount("/assets", StaticFiles(directory=str(_DIST / "assets")), name="assets")


def with_client(callable_fn):
    client = DramaBoxClient()
    try:
        return callable_fn(client)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    finally:
        client.close()


@app.get("/")
def home():
    index_file = _DIST / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return JSONResponse(
        {
            "message": "Frontend belum dibuild. Jalankan: cd frontend && npm install && npm run build",
        },
        status_code=200,
    )


@app.post("/api/search")
def api_search(payload: SearchPayload):
    return with_client(lambda c: c.search(payload.keyword, payload.page, payload.size))


@app.post("/api/latest")
def api_latest(payload: ListPayload):
    return with_client(lambda c: c.latest(payload.page, payload.size))


@app.get("/api/detail/{drama_id}")
def api_detail(drama_id: str):
    return with_client(lambda c: c.detail(drama_id))


@app.get("/api/episodes/{drama_id}")
def api_episodes(drama_id: str, page: int = 1, size: int = 100):
    return with_client(lambda c: c.episodes(drama_id, page, size))
