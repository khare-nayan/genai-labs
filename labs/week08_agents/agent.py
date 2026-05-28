from utils.llm_client import chat

def calculator(expression):
    return str(eval(expression))

def agent(query):
    if "calculate" in query:
        expr = query.split("calculate")[-1]
        return calculator(expr)
    else:
        return chat(query)

print(agent("calculate 5 * 10"))
print(agent("Explain AI"))