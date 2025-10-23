message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#prompting a user for their name and greeting them
name = input("Please enter your name: ")
print(f"Hello, {name}")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your name?"

name = input(prompt)
print(f"Hello, {name}!")