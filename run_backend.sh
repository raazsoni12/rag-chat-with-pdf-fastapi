#!/bin/bash
echo "Freeing port 8000..."
lsof -ti tcp:8000 | xargs kill -9 2>/dev/null

echo "Starting FastAPI backend..."
uvicorn main:app --reload --port 8000

