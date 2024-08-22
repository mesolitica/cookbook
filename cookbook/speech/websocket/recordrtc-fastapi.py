apikey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Imh1c2Vpbi56b2wwNUBnbWFpbC5jb20iLCJ1dWlkIjoiMWQ1OWI1NzAtNTgwOS00NmFmLThmYjAtMzhiYWQzYjUyMGVjIn0.ctSLjeCfh-XwHtyOqya05xTpWZxW94vPanwlx7WLf9I'

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import asyncio
import websockets
import json
import base64
import numpy as np
import urllib.parse

html = """
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8" />
  <title>RecordRTC</title>

  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <script src="https://www.WebRTC-Experiment.com/RecordRTC.js"></script>
</head>

<body>

  <div>
    <h2>This website also able to support multi-users at the same time, you can test it by opening multi-tabs</h2>
    <h2>Your ID: <span id="ws-id"></span></h2>
    <button id="start-recording" disabled>Start Recording</button>
    <button id="stop-recording" disabled>Stop Recording</button>
    <br><br>Text:
    <div id="text"></div>
  </div>

  <script type="text/javascript">
    global_blob = null;
    global_files = null;
    var client_id = Date.now()
    const isLocalhost = location.protocol !== "https:"
    const protocol = isLocalhost ? 'ws://' : 'wss://';
    const domain = window.location.host;
    document.querySelector("#ws-id").textContent = client_id;
    const ws = new WebSocket(`${protocol}${domain}/ws/${client_id}`);
    ws.onopen = function (e) {
      startRecording.disabled = false;
      console.log('opened');
    };
    ws.onmessage = function (event) {
      document.getElementById('text').innerHTML += event.data + ' ';
    };
    function sendMessage(event) {
    }

    async function asyncSend(blob) {
      arr = await blob.arrayBuffer();
      base64String = btoa(String.fromCharCode.apply(null, new Uint8Array(arr)));
      ws.send(base64String);
    }

    const startRecording = document.getElementById('start-recording');
    const stopRecording = document.getElementById('stop-recording');
    let recordAudio;

    startRecording.onclick = function () {
      startRecording.disabled = true;

      // https://recordrtc.org/
      navigator.getUserMedia({
        audio: true
      }, function (stream) {

        recordAudio = RecordRTC(stream, {
          type: 'audio',
          mimeType: 'audio/webm',
          sampleRate: 44100,
          desiredSampRate: 16000,

          recorderType: StereoAudioRecorder,
          numberOfAudioChannels: 1,
          timeSlice: 100,
          ondataavailable: function (blob) {
            asyncSend(blob);
            global_blob = blob;
          }
        });

        recordAudio.startRecording();
        stopRecording.disabled = false;
      }, function (error) {
        console.error(JSON.stringify(error));
      });
    };

    stopRecording.onclick = function () {
      startRecording.disabled = false;
      stopRecording.disabled = true;
      recordAudio.stopRecording(function () {
        recordAudio.getDataURL(function (audioDataURL) {
          var files = {
            audio: {
              type: recordAudio.getBlob().type || 'audio/wav',
              dataURL: audioDataURL
            }
          };
          console.log(files);
          global_files = files;

        });
      });
    };
  </script>

</body>

</html>
"""

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