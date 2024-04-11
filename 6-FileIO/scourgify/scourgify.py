import csv
import sys


def main():
    try:
        if sys.argv[1].endswith(".csv") and len(sys.argv) == 3:
            try:
                with open(sys.argv[1], "r") as file:
                    # Skip the header line
                    next(file)

                    students = []
                    for line in file:
                        f, l, h = line.rstrip().split(",")
                        student = {"f": f, "l": l, "h": h}
                        students.append(student)

                    with open(sys.argv[2], "a") as outfile:
                        fieldnames = ["f", "l", "h"]
                        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                        writer.writerows(students)
                        print("yes")

            except FileNotFoundError:
                print("File does not exist")
                sys.exit()

        elif len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit()

        else:
            print("Not a CSV file")
            sys.exit()

    except IndexError:
        print("Too few command-line arguments")
        sys.exit()


if __name__ == "__main__":
    main()
