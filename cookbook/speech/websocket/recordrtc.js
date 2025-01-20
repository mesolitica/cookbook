const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const url = require('url');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ noServer: true });

const apikey = '';
const base_url = "wss://api.mesolitica.com/audio/transcriptions/ws";

// Check parameter at https://api.mesolitica.com/scalar#tag/audio-transcription/POST/audio/transcriptions
const params = new URLSearchParams({
    "apikey": apikey,
    "language": "en"
});

const uri = `${base_url}?${params}`;

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

server.on('upgrade', (request, socket, head) => {
    const pathname = url.parse(request.url).pathname;

    if (pathname.startsWith('/ws/')) {
        const client_id = pathname.split('/')[2];

        wss.handleUpgrade(request, socket, head, (ws) => {
            wss.emit('connection', ws, request, client_id);
        });
    } else {
        socket.destroy();
    }
});

wss.on('connection', (ws, req) => {
    const websocket_api = new WebSocket(uri);

    ws.on('message', async (message) => {
        websocket_api.send(message.toString());
    });

    websocket_api.on('message', (message) => {
        ws.send(message.toString());
    });

    ws.on('close', () => {
        websocket_api.close();
    });
});

server.listen(3000, () => {
    console.log('Server is listening on port 3000');
});