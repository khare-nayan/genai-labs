def is_safe(text):
    banned = ["hack", "attack"]
    return not any(word in text.lower() for word in banned)

user_input = input("Enter prompt: ")

if is_safe(user_input):
    print("Safe to proceed")
else:
    print("Blocked due to unsafe content")