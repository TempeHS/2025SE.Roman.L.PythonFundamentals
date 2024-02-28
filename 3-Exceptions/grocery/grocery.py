def main():

    mycoollist = {}

    while True:
        try:
            item = input("grocery list: ").upper()

            if item in mycoollist:
                mycoollist[item] += 1
            else:
                mycoollist[item] = 1

        except EOFError:
            print("")
            for key in sorted(mycoollist.keys()):
                print(f"{mycoollist[key]} {key}")
            break


if __name__ == "__main__":
    main()
