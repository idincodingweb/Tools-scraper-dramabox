# DramaBox Scraper (Backend + React Frontend)

Project ini sekarang menggunakan arsitektur modern:
- **Backend API**: FastAPI (`dramabox_scraper/web.py`)
- **Frontend**: React + Vite modular (`frontend/`) dengan komponen gaya **shadcn/ui**
- **Core scraper client**: signed request HMAC SHA256 (`dramabox_scraper/client.py`)

## 1) Install backend
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2) Konfigurasi
```bash
cp .env.example .env
```

## 3) Jalankan frontend (React)
```bash
cd frontend
npm install
npm run dev
```
Frontend dev: `http://localhost:5173`

## 4) Jalankan backend (FastAPI)
```bash
uvicorn dramabox_scraper.web:app --reload --host 0.0.0.0 --port 8000
```
Backend API: `http://localhost:8000`

## 5) Build frontend untuk production
```bash
cd frontend
npm run build
```
Setelah build, backend otomatis serve `frontend/dist` pada route `/`.

## Endpoint API
- `POST /api/search`
- `POST /api/latest`
- `GET /api/detail/{drama_id}`
- `GET /api/episodes/{drama_id}`

## Struktur frontend modular
- `frontend/src/components/search-panel.tsx`
- `frontend/src/components/detail-panel.tsx`
- `frontend/src/components/ui/*` (Button, Input, Card)
- `frontend/src/App.tsx`
