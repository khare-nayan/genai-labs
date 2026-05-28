from utils.llm_client import chat

def summarize(text, style="short"):
    prompt = f"Summarize this text in {style} format:\n{text}"
    return chat(prompt)

if __name__ == "__main__":
    text = open("../../data/raw/sample_text.txt").read()
    print(summarize(text, "bullet points"))