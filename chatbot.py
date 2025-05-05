import re

# Additional custom responses
responses = {
    "hi": "Hello! How can I assist you today?",
    "how are you": "I'm doing great, thank you! How about you?",
    "bye": "Goodbye! Have a great day ahead!",
    "your name": "I am ChatNLP, your virtual assistant.",
    "what is your purpose": "I can help you with a variety of tasks like answering questions, providing information, and much more!",
    "help": "How can I assist you? Feel free to ask me anything.",
    "thank you": "You're welcome! Let me know if you need anything else.",
    "who are you": "I am an AI chatbot created to assist with your queries.",
    "what can you do": "I can answer questions, tell jokes, and even help you with some basic tasks. Try asking me anything!",
    "how is the weather": "I currently cannot check the weather, but you can try checking an online service for live updates.",
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "tell me a story": "Once upon a time, in a land full of tech geeks, there was a chatbot who helped everyone with their coding problems. Everyone loved ChatNLP!",
    "what is your favorite color": "I like all colors, but blue is a soothing one, don't you think?",
    "can you help with coding": "Yes, I can help with Python, Java, HTML, CSS, and even more. What do you need help with?",
    "what is the capital of france": "The capital of France is Paris.",
    "how old are you": "I am timeless! I don't age, I'm just a program that always learns!",
    "can you calculate": "Yes, I can do basic math! Try asking me a math question.",
    "what is the meaning of life": "The meaning of life is to live it to the fullest, learn, grow, and help others around you.",
    "do you have emotions": "I don't have emotions, but I can understand them and try to help you based on how you feel.",
    "tell me a fact": "Did you know? The Eiffel Tower can be 15 cm taller during the summer due to the expansion of iron in the heat."
}

def chatbot_response(user_input):
    # Lowercase the input for case-insensitive matching
    user_input = user_input.lower()

    # Match the input with the responses dictionary
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response
    
    # If no match is found
    return "I'm sorry, I didn't understand that. Can you rephrase?"

def chat():
    print("ChatNLP: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("ChatNLP: Goodbye! Have a great day ahead!")
            break
        else:
            print("ChatNLP:", chatbot_response(user_input))

# Start the chatbot
chat()
