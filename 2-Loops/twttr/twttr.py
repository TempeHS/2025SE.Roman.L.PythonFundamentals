# owo

vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]


def main():
    elonmusk = input("str of text: ")

    for char in elonmusk:
        if char in vowels:
            elonmusk = elonmusk.replace(char, "")

    print(elonmusk)


main()
