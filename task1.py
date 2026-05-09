# =========================================================
# DECODEBOT - Advanced Rule-Based AI Chatbot (Python)
# DecodeLabs Internship Project 1
# =========================================================

import random
import time

#knowledge base

responses = {

    "hello": [
        "Hey there! I'm AskIt. How can I help you today?",
        "Hello! Ready to build some AI today?"
    ],

    "hi": [
        "Hi! Great to see you.",
        "Hey! What's on your mind?"
    ],

    "hey": [
        "Hey! AskIt here.",
        "Hey there 👋"
    ],

    "what is your name": [
        "My name is AskIt - your AI assistant."
    ],

    "who are you": [
        "I'm AskIt, a deterministic rule-based chatbot."
    ],

    "who made you": [
        "I was built using Python and logic-based AI concepts by Noor."
    ],

    "what is ai": [
        "Artificial Intelligence is the simulation of human intelligence by machines."
    ],

    "what is machine learning": [
        "Machine Learning allows systems to learn patterns from data."
    ],

    "what is chatbot": [
        "A chatbot is a program that simulates human conversation."
    ],

    "what is hashmap": [
        "A HashMap or Dictionary stores key-value pairs for fast O(1) lookup."
    ],

    "what is project 1": [
        "Project 1 is a Rule-Based AI Chatbot using control flow and logic."
    ],

    "what is ipo model": [
        "IPO means Input → Process → Output."
    ],

    "what is sanitization": [
        "Sanitization means cleaning user input using lowercase conversion and trimming spaces."
    ],

    "tell me a joke": [
        "Why do programmers hate nature? Too many bugs 🐛"
    ],

    "tell me a fact": [
        "Fun fact: Python was named after Monty Python, not the snake!"
    ],

    "help": [
        """
Available Commands:

• Greetings:
  hello, hi, hey

• AI Topics:
  what is ai
  what is machine learning
  what is chatbot

• Internship:
  what is project 1
  what is ipo model

• Fun:
  tell me a joke
  tell me a fact

• Exit:
  exit or quit
"""
    ]
}

#Input Sanitization

def sanitize_input(user_input):

    cleaned_input = user_input.lower().strip()

    return cleaned_input

#Typing effect

def typing_effect(message):

    print("\nAskIt: ", end="")

    for char in message:
        print(char, end="", flush=True)
        time.sleep(0.02)

    print("\n")

#Response Engine

def get_response(user_input):

    if user_input in responses:

        return random.choice(responses[user_input])

    for key in responses:

        if key in user_input:

            return random.choice(responses[key])

    return "I don't understand that yet. Type 'help' to see available commands."

# BANNER

def show_banner():

    print("=" * 60)
    print("        AskIt - RULE-BASED AI CHATBOT")
    print("          DecodeLabs Internship Project 1")
    print("=" * 60)

    print("\nType 'help' to see commands.")
    print("Type 'exit' to quit.\n")

# MAIN CHATBOT SYSTEM

def chatbot():

    show_banner()

    message_count = 0

    while True:

        raw_input_text = input("You: ")

        user_input = sanitize_input(raw_input_text)

        if user_input == "":

            print("\nAskIt: Please type something.\n")
            continue

        if user_input in ["exit", "quit"]:

            print("\nAskIt: Session ended successfully.")
            print(f"Total messages exchanged: {message_count}")

            break

        response = get_response(user_input)

        typing_effect(response)

        message_count += 1

# PROGRAM START

chatbot()