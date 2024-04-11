def main():
    try:
        while True:
            picknumber = int(
                input("1) add name\n2) remove\n3) iterate test\n4) quit\n")
            )

            if picknumber == 1:
                add_name()
                break
            elif picknumber == 2:
                remove()
                break
            elif picknumber == 3:
                three()
                break
            elif picknumber == 4:
                quit()
                break
            else:
                True

    except ValueError:
        True


def add_name():
    name = input("what is your name?: ")

    with open("test.txt", "r") as file:
        for line in file:
            if name in line:
                print("already there")

            else:
                with open("test.txt", "a") as file:
                    file.write(f"{name}\n")
                    file.close()

                print(f"{name} is imported")

    main()


def remove():
    with open("test.txt", "w") as file:
        file.write("")
        print("cleared")

    main()


def three():
    numbers = ["1", "2", "3"]
    print(numbers)
    num = input("say numbers: ")
    found = False
    for char in num:
        if char in numbers:
            found = True

    if not found:
        print("number not found")

    else:
        print(f"number {char} found")

    main()


def quit():
    print("you quit")


if __name__ == "__main__":
    main()
