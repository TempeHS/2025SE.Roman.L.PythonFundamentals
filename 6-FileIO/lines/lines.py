import sys


def main():
    try:
        if sys.argv[1].endswith(".py") and len(sys.argv) == 2:

            count = 0

            try:
                with open(sys.argv[1]) as file:
                    for line in file:
                        line = line.lstrip()
                        if not line.startswith("#") and line.strip():

                            count += 1

                print(f"{count} lines of code.")

            except FileNotFoundError:
                print("File does not exist")
                sys.exit

        elif len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit

        else:
            print("Not a Python file")
            sys.exit

    except IndexError:
        print("Too few command-line arguments")
        sys.exit


if __name__ == "__main__":
    main()
