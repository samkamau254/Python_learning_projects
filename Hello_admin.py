usernames = ['peter', 'john', 'luke', 'mathew', 'andrew', 'admin']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")

usernames = []

if usernames:
    print(f"Hello")
else:
    print("We need usernames!")
    
    