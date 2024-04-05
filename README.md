# Nous

All related to Nous, MaLLaM 🌙, Speech, Translation, cookbooks 📖 , bugs 🐛 and feature requests 🙇🏽. This repository only applicable for commercial models from https://mesolitica.com, not open models from https://mesolitica.com/opensource

## MaLLaM 🌙

MaLLaM 🌙 is Multi-lingual Malaysian Chat Language Model, 32k context length, Malaysian centric and private, in the future we will support longer context length and code interpreter, get your API key at https://app.nous.mesolitica.com/

### OpenAI compatible

MaLLaM 🌙 is compatible with OpenAI library,

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://llm-router.nous.mesolitica.com",
)
```

or if you prefer CURL command, read the API documentation at https://llm-router.nous.mesolitica.com/scalar

**Currently we only support Chat Completion**.

### [Cookbook](cookbook)

We covered RAG, JSON prompts and so much more.

### Evaluation

1. [json-mode-eval](evaluation/json-mode-eval),

Originally from https://huggingface.co/datasets/NousResearch/json-mode-eval, this test is to test how good the models able to convert human natural text into JSON output given the OpenAPI schema.

## Self-hosted Enterprise

If you are interested to self-host Nous in your virtual private network, Contact us at khalil@mesolitica.com or husein@mesolitica.com to know more.

### What do you get

1. ♾️ usage of all quota, MaLLaM 🌙, Speech, Translation and chatbots.
2. Up-to-date enterprise versioning including evolution of MaLLaM 🌙, Speech, Translation and chatbots.
3. Can be either on private cloud or on premise, Dashboard and all the APIs will be hosted using virtual private IP.

### Hardware

1. If you do not have hardware accelerator, we partner with NVIDIA APAC to include hardware solution with support.
2. Bring your own hardware accelerator, we do not provide support.

### Software

We provide quarterly and yearly licensing, and yearly licencing is much more cheaper in the long term, include support.
