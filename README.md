# AQI AI Backend (Clean)

Clean FastAPI backend you can run locally and later connect to:
- Wokwi (ESP32 sensor simulation)
- Unity (sprinkler animation)
- Govt AQI API (optional)

## Prereqs
Install **Python 3.12** (recommended) or **Python 3.11**.
Avoid Python 3.14 for now (many packages don’t support it yet).

## Setup (Windows PowerShell)
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Where to put Govt API key?
Copy `.env.example` to `.env`:
```powershell
copy .env.example .env
```
Put your key inside `.env`:
GOV_AQI_API_KEY=YOUR_KEY_HERE
GOV_AQI_API_URL=https://... (if you have a URL)

## Run
```powershell
uvicorn app.main:app --reload
```
Open Swagger UI: http://127.0.0.1:8000/docs

## Notes
- Empty `__init__.py` files are normal: they mark folders as Python packages.
