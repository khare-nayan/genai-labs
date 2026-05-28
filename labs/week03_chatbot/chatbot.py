from utils.llm_client import chat

history = []

def chatbot():
    while True:
        user_input = input("You: ")
        history.append(f"User: {user_input}")
        
        prompt = "\n".join(history)
        response = chat(prompt)
        
        history.append(f"Bot: {response}")
        print("Bot:", response)

if __name__ == "__main__":
    chatbot()