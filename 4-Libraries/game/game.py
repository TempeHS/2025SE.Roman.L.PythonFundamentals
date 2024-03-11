import random


def main():
    while True:
        try:
            prompt = input("Level: ")

            if int(prompt) < 0:
                main()

        except ValueError:
            print("a")


if __name__ == "__main__":
    main()
