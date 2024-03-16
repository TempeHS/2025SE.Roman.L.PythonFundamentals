def main():
    greet = input("hi say something: ").lower()
    money = value(greet)
    print(money)


def value(greet):
    if greet.startswith("hello"):
        money = "$0"
    elif greet.startswith("h"):
        money = "$20"
    else:
        money = "$100"

    return money


if __name__ == "__main__":
    main()
