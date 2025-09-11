import os
from dotenv import find_dotenv, load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables
load_dotenv(find_dotenv())

# Hugging Face API token
API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
MODEL_ID = "google/gemma-2-2b-it"  # You can choose any model

# Initialize client
client = InferenceClient(
    provider="nebius",
    api_key=API_TOKEN,
)

# Chatbot conversation loop
def chat():
    print("Hi! I'm your chatbot. Type 'exit' to quit.\n")
    
    # Keep track of conversation messages
    conversation_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        conversation_history.append({"role": "user", "content": user_input})
        print("Chatbot is thinking...")
        completion = client.chat.completions.create(
            model=MODEL_ID,
            messages=conversation_history[-10:], # last 10 messages for context
        )
        
        bot_response = completion.choices[0].message["content"]
        print(f"Chatbot: {bot_response}")
        
        conversation_history.append({"role": "assistant", "content": bot_response})


# Start the chatbot
chat()
