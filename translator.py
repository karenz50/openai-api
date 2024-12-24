from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def translate_text(text, target_language):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are a helpful assistant, please return only the translation."},
                  {"role": "user", "content": f"Translate the following text to {target_language}: {text}"}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    text = input("Enter some text: ")
    target_language = input("Enter target language: ")
    translation = translate_text(text, target_language)
    print("Translation:", translation)