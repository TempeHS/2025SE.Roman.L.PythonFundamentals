# ask for name
name = input("What your name? ").strip().title()

# split user name to first n last name
first, last = name.split(" ")

# say hello to user
print(f"hello, {name}")
