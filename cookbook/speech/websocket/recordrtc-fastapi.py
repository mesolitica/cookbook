apikey = ''

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import asyncio
import websockets
import json
import base64
import numpy as np
import urllib.parse

app = FastAPI()

base_url = "wss://llm-router.nous.mesolitica.com/audio/transcriptions/ws"

# check parameter at https://llm-router.nous.mesolitica.com/scalar#tag/audio-transcription/POST/audio/transcriptions
params = {
    "apikey": apikey,
    "language": "en"
}

uri = f"{base_url}?{urllib.parse.urlencode(params)}"

@app.get('/')
async def get():
    with open('index.html') as fopen:
        html = fopen.read()
    return HTMLResponse(html)

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket, client_id):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket, client_id):
        try:
            await websocket.close()
        except BaseException as e:
            pass

        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
        await asyncio.sleep(0)


manager = ConnectionManager()


async def send_message(websocket, websocket_api):
    while True:
        arr_base64 = await websocket.receive_text()
        await websocket_api.send(arr_base64)
        await asyncio.sleep(0)

async def receive_message(websocket, websocket_api):
    while True:
        output = await websocket_api.recv()
        await asyncio.sleep(0)
        
        await manager.send_personal_message(output, websocket)

@app.websocket('/ws/{client_id}')
async def websocket_endpoint(websocket: WebSocket, client_id: int):

    await manager.connect(websocket, client_id=client_id)
    try:
        async with websockets.connect(uri) as websocket_api:
            await asyncio.gather(
                send_message(websocket, websocket_api),
                receive_message(websocket, websocket_api)
            )

    except WebSocketDisconnect:
        await manager.disconnect(websocket, client_id=client_id)