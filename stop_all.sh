#!/bin/bash

echo "🛑 Stopping FastAPI + Streamlit..."

lsof -ti tcp:8000 | xargs kill -9 2>/dev/null
lsof -ti tcp:8501 | xargs kill -9 2>/dev/null

echo "✅ All services stopped."

