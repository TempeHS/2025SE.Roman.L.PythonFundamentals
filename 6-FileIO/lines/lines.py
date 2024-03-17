import sys


def main():
    try:
        if sys.argv[1].endswith(".py") and len(sys.argv) == 2:
            count = 0
            try:
                with open(sys.argv[1]) as file:
                    for line in file:
                        line = line.lstrip()
                        # line strip considered false if line is empty
                        if not line.startswith("#") and line.strip():
                            count += 1
                print(f"{count} lines of code.")

            except FileNotFoundError:
                print("File does not exist")
                sys.exit

        elif len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit

        if ".py" not in sys.argv[1]:
            print("Not a Python file")
            sys.exit

        else:
            sys.exit

    except IndexError:
        print("Too few command-line arguments")
        sys.exit


if __name__ == "__main__":
    main()
