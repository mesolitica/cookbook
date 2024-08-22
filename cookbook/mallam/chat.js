const OpenAI = require('openai');

const openai = new OpenAI({
    baseURL: 'https://llm-router.nous.mesolitica.com',
});

async function main() {
    const completion = await openai.chat.completions.create({
        model: "mallam-small",
        messages: [
            { "role": "system", "content": "Awak pembantu AI yang berguna." },
            { "role": "user", "content": "Hello!" }
        ],
    });

    console.log(completion.choices[0]);
}

main();