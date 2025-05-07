import openai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_ovidiu(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # This is your assigned model
        messages=[
            {"role": "system", "content": "You are Ovidiu, a confident, funny, and ethical dating coach."},
            {"role": "user", "content": question}
        ],
        temperature=0.8,
        max_tokens=300,
    )
    return response['choices'][0]['message']['content']

# Test the chatbot
if __name__ == "__main__":
    while True:
        user_input = input("Ask Ovidiu: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("Ovidiu:", ask_ovidiu(user_input))
