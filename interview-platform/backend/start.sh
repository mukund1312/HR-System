
#!/bin/bash

set -e

cd "$(dirname "$0")"

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    uv venv
fi

echo "Installing dependencies..."
uv sync

# uv run alembic init alembic

echo "Running database migrations..."
uv run alembic upgrade head

echo "Starting FastAPI server..."
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
