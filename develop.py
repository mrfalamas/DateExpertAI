import os
import json
from openai import OpenAI
from dotenv import load_dotenv
import tkinter as tk

# Load my api saved in .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

functions = [
    {
        "name": "get_restaurant_around",
        "description": "Finds 3 nice restaurants around a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The name of the city or area to search."
                }
            },
            "required": ["location"]
        }
    }
]

def ask_ovidiu(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Ovidiu, a confident, modern dating coach. "
                    "You speak respectfully and give fun, smart, age-appropriate advice. "
                    "Avoid anything unethical or unsafe, especially when dealing with young people."
                )
            },
            {"role": "user", "content": question}
        ],
        functions=functions,
        function_call="auto",
        temperature=0.8,
        max_tokens=300,
    )

    choice = response.choices[0]

    message = getattr(choice, "message", None)

    if message is None:
        return "No message returned by the model."

    if message.content:
        return message.content
    elif message.function_call:
        return f"[Function call] Name: {message.function_call.name}, Arguments: {message.function_call.arguments}"
    else:
        return "Sorry, I didn't get that."

# Ask ovidiu is called directly in main
if __name__ == "__main__":
    print("Welcome to DateExpertAI. Ask Ovidiu anything. Type 'exit/bye/quit' to quit.\n")
    while True:
        user_input = input("Your question: ")
        if user_input in ["Exit","exit","bye","Bye","Quit","quit"]:
            print("Goodbye!")
            break
        try:
            reply = ask_ovidiu(user_input)
            print("\nOvidiu:", reply, "\n")
        except Exception as e:
            print("Error:", e)