# MaLLaM 🌙

All related to MaLLaM 🌙 Malaysia Large Language Models, cookbooks 📖 , bugs 🐛 and feature requests 🙇🏽. This repository only applicable for commercial models from https://mesolitica.com/mallam, not open models https://mesolitica.com/openmodel

MaLLaM 🌙 is Multi-lingual Malaysian Chat Language Model, 32k context length, Malaysian centric and private, in the future we will support longer context length and code interpreter, get your API key at https://app.nous.mesolitica.com/

## OpenAI compatible

MaLLaM 🌙 is compatible with OpenAI library,

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://llm-router.nous.mesolitica.com",
)
```

or if you prefer CURL command, read the API documentation at https://llm-router.nous.mesolitica.com/scalar

**Currently we only support Chat Completion**.

## Evaluation

1. [json-mode-eval](evaluation/json-mode-eval),

Originally from https://huggingface.co/datasets/NousResearch/json-mode-eval, this test is to test how good the models able to convert human natural text into JSON output given the OpenAPI schema.
