def main():
    add = int(input("Number: "))
    with open("myfile.txt", "r") as file:
        for line in file:
            number = int(line)

            result = (number) + (add)

    with open("myfile.txt", "w") as file:
        file.write(f"{result}\n")
        file.close()

        print(result)


if __name__ == "__main__":
    main()
