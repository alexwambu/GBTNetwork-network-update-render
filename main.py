from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import json

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "GBTNetwork RPC is live", "rpc_url": os.getenv("RPC_URL")}

@app.get("/chain-info")
def chain_info():
    return {
        "chainId": os.getenv("CHAIN_ID", "999"),
        "rpc": os.getenv("RPC_URL"),
        "currency": os.getenv("CURRENCY_SYMBOL", "GBT")
    }

@app.get("/metadata")
def metadata():
    with open("metadata.json") as f:
        return json.load(f)
