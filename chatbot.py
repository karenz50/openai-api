from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("Chatbot (type quit to exit)")
    while True:
        print("----------------------------------")
        user_input = input("User: ")
        if "quit" == user_input.lower():
            break
        response = chat_gpt(user_input)
        print("Bot:", response)