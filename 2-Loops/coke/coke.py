def main():
    (due) = int(50)
    (paid) = int(0)

    while True:
        moneymaker = int(input("Insert Coin: "))
        if due > 0 and moneymaker == 25 or moneymaker == 10 or moneymaker == 5:
            due -= moneymaker
            paid += moneymaker
            if paid >= 50:
                print(f"Change Owed: {paid - 50}")
                break
            else:
                print(f"Amount Due: {due}")

        else:
            print(f"Amount Due: {due}")


main()
