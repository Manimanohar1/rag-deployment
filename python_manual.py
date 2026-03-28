##Python to interact with the Ollama and train the vector DB

#!/usr/bin/env python3
import requests

url = "http://172.20.93.175:11434/api/generate"

print("--- AI Infrastructure CLI Online ---")
print("Type 'exit' to terminate the connection.\n")

while True:
    user_prompt = input("You: ")

    if user_prompt.lower() == 'exit':
        print("Terminating loop. Goodbye.")
        break
    payload = {
        "model": "tinyllama",
        "prompt": user_prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        output = response.json()
        print(f"AI: {output['response']}\n")
    except Exception as e:
        print(f"Network routing failed: {e}\n")
