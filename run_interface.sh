#!/bin/bash

if [ ! -d ".venv" ]; then
    # create virtualenv
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install uv
    uv sync
fi

source .venv/bin/activate
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
