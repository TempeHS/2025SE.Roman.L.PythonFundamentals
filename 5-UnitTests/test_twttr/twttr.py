# forgot to remove that

vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]


def main():
    elonmusk = input("str of text: ")
    real = shorten(elonmusk)
    print(real)


def shorten(elonmusk):
    for char in elonmusk:
        if char in vowels:
            elonmusk = elonmusk.replace(char, "")
    return elonmusk


if __name__ == "__main__":
    main()
