from utils.llm_client import chat

prompts = [
    "Explain AI",
    "Explain AI in simple terms for a child",
    "Explain AI with examples",
    "Explain AI in 3 bullet points",
]

for p in prompts:
    print("\n--- Prompt ---")
    print(p)
    print("\n--- Response ---")
    print(chat(p))