#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run FastAPI app with Uvicorn
uvicorn main:app --host 127.0.0.1 --port 8000
