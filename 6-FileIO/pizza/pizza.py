import sys
import csv
from tabulate import tabulate


def main():
    try:
        if sys.argv[1].endswith(".csv") and len(sys.argv) == 2:
            try:
                with open(sys.argv[1]) as file:
                    reader = csv.reader(file)
                    pizzas = []

                    for row in reader:
                        pizzas.append(row)

                    print(tabulate(pizzas, tablefmt="grid"))

            except FileNotFoundError:
                print("File does not exist")
                sys.exit

        elif len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit

        else:
            print("Not a CSV file")
            sys.exit

    except IndexError:
        print("Too few command arguments")
        sys.exit


if __name__ == "__main__":
    main()
