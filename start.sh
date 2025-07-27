#!/bin/bash
echo "Starting GBTNetwork RPC Server..."
uvicorn main:app --host 0.0.0.0 --port 10000
