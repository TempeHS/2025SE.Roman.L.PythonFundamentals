import inflect

p = inflect.engine()
mycoollist = []


def main():
    while True:
        try:
            item = input("")
            mycoollist.append(item)

        except EOFError:
            adieu = p.join(mycoollist)
            print(f"Adieu, adieu, to {adieu}")
            break


if __name__ == "__main__":
    main()
