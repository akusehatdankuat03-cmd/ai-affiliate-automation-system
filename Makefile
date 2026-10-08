PYTHON ?= python3
PIP ?= $(PYTHON) -m pip

help:
	@echo "Usage: make setup | make backend | make frontend | make test | make down"

setup:
	@echo "Installing Python dependencies..."
	cd backend && $(PIP) install -r requirements.txt
	@echo "Setup complete. Copy .env.example to .env and adjust values."

backend:
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

frontend:
	cd frontend && npm install && npm run dev

test:
	cd backend && pytest

down:
	docker compose down -v
