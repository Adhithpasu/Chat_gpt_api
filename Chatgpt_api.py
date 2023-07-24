import os
import openai
openai.api_key = os.getenv("Api_key")
messages = [{"role": "system", "content": "You are a helpful teacher"}]
while True:
    message = input('User: ')
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=messages)
    reply = chat.choices[0].message.content
    print(f'Chat:{reply}')
    messages.append({"role": "assistant", "content": reply})

