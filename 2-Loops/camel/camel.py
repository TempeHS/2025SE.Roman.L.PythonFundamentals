def main():
    x = input("Name in camel case?: ")
    for letter in x:
        if letter.isupper():
            print("_" + letter.lower(), end="")
        else:
            print(letter, end="")


if __name__ == "__main__":
    main()
