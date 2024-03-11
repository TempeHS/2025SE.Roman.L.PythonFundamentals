import random


def main():
    count = 0
    ranger = 0

    while True:
        try:
            if count == 0:
                n = input("Level: ")
                thisisanint = int(n)

                if n.isalnum():
                    count += 1

                else:
                    count = 0

            if count == 1:
                if ranger == 0:
                    ranger = random.randint(1, thisisanint)

                else:
                    e = input("Guess: ")
                    guess = int(e)

                    if e.isalnum():
                        count += 1

                    else:
                        count = 1

            # guess for int
            if count == 2:
                if ranger == guess:
                    print("Just right!")
                    break
                elif ranger > guess:
                    print("Too small!")
                    break
                else:
                    print("Too large!")
                    break

        except ValueError:
            count == count


if __name__ == "__main__":
    main()
