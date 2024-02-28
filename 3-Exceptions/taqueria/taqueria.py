def main():

    dict = {
        "baja taco": 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00,
    }

    realtotal = 0

    while True:

        try:
            item = input("Place an order: ").lower()
            for char in item:
                if item in dict:
                    total = dict[item]

                    realtotal += total

                    print(f"Total: ${realtotal:.2f}")
                    break

        except EOFError:
            print("\n")
            break


if __name__ == "__main__":
    main()
