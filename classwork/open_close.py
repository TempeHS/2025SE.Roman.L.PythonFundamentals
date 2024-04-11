def main():
    while True:
        add = int(input("Number: "))
        with open("myfile.txt", "r") as file:
            for line in file:
                try:
                    lista = []

                    number = int(line)

                    if number > 10:
                        print("Above 10")
                        False

                    elif number <= 10:
                        result = (number) + (add)

                        lista.append(result)

                        with open("myfile.txt", "w") as file:
                            file.write(f"{result}\n")
                            file.close()

                            print(result)
                            print(lista)

                except ValueError:
                    print("Above 10")


if __name__ == "__main__":
    main()
