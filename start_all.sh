#!/bin/bash

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_DIR" || exit 1

echo "✅ Activating virtual environment..."
source venv/bin/activate

echo "🧹 Freeing ports (8000 for FastAPI, 8501 for Streamlit)..."
lsof -ti tcp:8000 | xargs kill -9 2>/dev/null
lsof -ti tcp:8501 | xargs kill -9 2>/dev/null

echo "🚀 Starting FastAPI backend on http://127.0.0.1:8000 ..."
uvicorn main:app --reload --port 8000 > backend.log 2>&1 &
BACKEND_PID=$!

sleep 2

echo "🎛 Starting Streamlit frontend on http://localhost:8501 ..."
streamlit run streamlit_app.py > frontend.log 2>&1 &
FRONTEND_PID=$!

# Wait a bit to ensure services are up
sleep 3

echo ""
echo "✅ Project Started Successfully!"
echo "   Backend Docs : http://127.0.0.1:8000/docs"
echo "   Frontend UI  : http://localhost:8501"
echo ""
echo "📌 Logs:"
echo "   backend.log  |  frontend.log"
echo ""
echo "🛑 To stop everything, run: ./stop_all.sh"
echo ""

# Auto-open browser tabs (Mac)
echo "🌐 Opening in browser..."
open -a "Google Chrome" "http://127.0.0.1:8000/docs"
open -a "Google Chrome" "http://localhost:8501"


wait


