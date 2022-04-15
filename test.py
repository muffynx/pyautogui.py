for attempt in range(5):
    password = input('What is your password?')
    if password == "abc123":
        print("Welcome!")
        break
else:
    print("all out of password guesses")