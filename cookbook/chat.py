from openai import OpenAI

client = OpenAI(
    base_url="https://llm-router.nous.mesolitica.com",
)

completion = client.chat.completions.create(
  model="mallam-small",
  messages=[
    { "role": "system", "content": "Awak pembantu AI yang berguna." },
    { "role": "user", "content": "Hello!" }
  ]
)
print(completion.choices[0].message)