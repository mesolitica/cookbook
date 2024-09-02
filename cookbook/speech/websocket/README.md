# Websocket streaming

## Some tips

For Mesolitica Websocket Speech API, because the API support streaming token, so the sender and listener must run on different loop.

## PyAudio inferface -> Websocket python

[pyaudio-websocket.ipynb](pyaudio-websocket.ipynb).

https://github.com/user-attachments/assets/2f10d2c9-90b8-4561-97e5-872469732ba1

## RecordRTC JS -> Websocket FastAPI

[recordrtc-fastapi.py](recordrtc-fastapi.py).

1. Basically, Frontend RecordRTC JS -> (Websocket) FastAPI -> (Websocket) Websocket Speech API.
2. The reason why you cannot call directly from Frontend is to prevent API key leakage to the users.

### how to run

1. Run FastAPI,

```bash
uvicorn recordrtc-fastapi:app --reload --host 0.0.0.0 --port 8000
```

2. Access http://localhost:8000,

https://github.com/user-attachments/assets/ac46fede-f6fe-43de-8333-f0b0f8f04bd3

## RecordRTC JS -> Websocket ExpressJS

1. Basically, Frontend RecordRTC JS -> (Websocket) ExpressJS -> (Websocket) Websocket Speech API.
2. The reason why you cannot call directly from Frontend is to prevent API key leakage to the users.

### how to run

1. Run Node JS,

```bash
npm install express ws
node recordrtc.js
```
