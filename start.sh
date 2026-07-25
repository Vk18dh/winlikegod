#!/bin/bash
# Start the Flask backend in the background
export FLASK_APP=frontend/app.py
export FLASK_ENV=development
echo "Starting Flask frontend server on port 5000..."
python frontend/app.py &

# Start an interactive bash shell
echo "Starting interactive bash shell..."
exec bash
