import random


def main():
    get_level()


def get_level():
    try:
        level = int(input("Level: "))
        generate_integer(level)

    except ValueError:
        get_level()


def generate_integer(level):

    count = 0
    score = 0
    wrong = 0

    # level to digit
    if level == 1:
        digit1 = random.randint(1, 9)
        digit2 = random.randint(1, 9)
    elif level == 2:
        digit1 = random.randint(10, 99)
        digit2 = random.randint(10, 99)
    elif level == 3:
        digit1 = random.randint(100, 999)
        digit2 = random.randint(100, 999)
    else:
        raise ValueError(get_level())

    realans = digit1 + digit2

    while True:
        if level == 1:
            try:
                answer = int(input(f"{digit1} + {digit2} = "))

                if answer == realans:
                    count += 1
                    score += 1
                    wrong = 0

                    digit1 = random.randint(1, 9)
                    digit2 = random.randint(1, 9)
                    realans = digit1 + digit2

                else:
                    wrong += 1
                    print("EEE")

                    if wrong == 3:
                        print(f"{digit1} + {digit2} = {realans}")
                        count += 1
                        wrong = 0

                        digit1 = random.randint(1, 9)
                        digit2 = random.randint(1, 9)
                        realans = digit1 + digit2

                    else:
                        wrong == wrong

                if count == 10:
                    print(score)
                    break

            except ValueError:
                pass

        elif level == 2:
            try:
                answer = int(input(f"{digit1} + {digit2} = "))

                if answer == realans:
                    count += 1
                    score += 1
                    wrong = 0

                    digit1 = random.randint(10, 99)
                    digit2 = random.randint(10, 99)
                    realans = digit1 + digit2

                else:
                    wrong += 1
                    print("EEE")

                    if wrong == 3:
                        print(f"{digit1} + {digit2} = {realans}")
                        count += 1
                        wrong = 0

                        digit1 = random.randint(10, 99)
                        digit2 = random.randint(10, 99)
                        realans = digit1 + digit2

                    else:
                        wrong == wrong

                if count == 10:
                    print(score)
                    break

            except ValueError:
                pass

        elif level == 3:
            try:
                answer = int(input(f"{digit1} + {digit2} = "))

                if answer == realans:
                    count += 1
                    score += 1
                    wrong = 0

                    digit1 = random.randint(100, 999)
                    digit2 = random.randint(100, 999)
                    realans = digit1 + digit2

                else:
                    wrong += 1
                    print("EEE")

                    if wrong == 3:
                        print(f"{digit1} + {digit2} = {realans}")
                        count += 1
                        wrong = 0

                        digit1 = random.randint(100, 999)
                        digit2 = random.randint(100, 999)
                        realans = digit1 + digit2

                    else:
                        wrong == wrong

                if count == 10:
                    print(score)
                    break

            except ValueError:
                pass


if __name__ == "__main__":
    main()
