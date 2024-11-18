# Cookbook

cookbooks 📖 for Mesolitica products! This repository only applicable for commercial models from https://mesolitica.com, not open models from https://mesolitica.com/opensource

## API key

Get your API key at https://app.nous.mesolitica.com/

## Documentation

We hosted scalar documentation at https://llm-router.nous.mesolitica.com/scalar

## Concurrency

All API support concurrency requests, it means,

1. If you have a batch of texts, you can fire multiple requests at the same without impacting the latency, same goes to Speech API.
2. For Websocket Speech API, you can connect multiple users from your side to do real-time audio streaming to the Websocket server.

## [MaLLaM 🌙](cookbook/mallam)

1. [Python OpenAI compatible]()
2. [Streaming Python OpenAI compatible]()
3. [RAG](cookbook/mallam/RAG.ipynb)
4. [JSON format](cookbook/mallam/JSON-format.ipynb)
5. [Function call](cookbook/mallam/function-call.ipynb)
6. [System prompt](cookbook/mallam/system-prompt.ipynb)

### [Evaluation](cookbook/mallam/evaluation)

1. [json-mode-eval](evaluation/json-mode-eval),

Originally from https://huggingface.co/datasets/NousResearch/json-mode-eval, this test is to test how good the models able to convert human natural text into JSON output given the OpenAPI schema.

## [Retrieval](cookbook/retrieval)

1. [Python OpenAI compatible]()

## [Speech](cookbook/speech)

1. [Python OpenAI compatible](cookbook/speech/python-openai.ipynb)
2. [Streaming using AIOHTTP](cookbook/speech/streaming-python.ipynb)
3. [Streaming using AIOHTTP with VAD](cookbook/speech/streaming-python-vad.ipynb)

For streaming, make sure read our [streaming documentation](cookbook/speech/streaming.md).

### [Streaming using Websocket](cookbook/speech/websocket)

1. [Microphone PyAudio -> Websocket Python](cookbook/speech/websocket/pyaudio-websocket.ipynb)

https://github.com/user-attachments/assets/067859ca-5c05-4704-9f22-33c28f0b57b5

2. [RecordRTC JS -> Websocket FastAPI](cookbook/speech/websocket/recordrtc-fastapi.py)

https://github.com/user-attachments/assets/6dba8a94-1953-4a52-9844-9955ca1e29ac

## [Translation](cookbook/translation)

1. [Python Requests]()

## Self-hosted Enterprise

If you are interested to self-host Mesolitica products in your virtual private network, Contact us at khalil@mesolitica.com or husein@mesolitica.com to know more.

### What do you get

1. ♾️ usage of all quota, MaLLaM 🌙, Speech, Translation and chatbots.
2. Up-to-date enterprise versioning including evolution of MaLLaM 🌙, Speech, Translation and chatbots.
3. Can be either on private cloud or on premise, Dashboard and all the APIs will be hosted using virtual private IP.

### Hardware

1. If you do not have hardware accelerator, we partner with NVIDIA APAC to include hardware solution with support.
2. Bring your own hardware accelerator, we do not provide support.

### Software

We only provide yearly licensing with starting specific amount.
