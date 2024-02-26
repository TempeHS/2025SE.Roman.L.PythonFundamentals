# percentage rounded to the nearest integer


def main():
    x = get_fuel()

    if 0 >= x >= 1:
        print("E")

    elif 99 >= x >= 100:
        print("F")

    elif x > 100:
        print("try again")
        main()

    elif x < 0:
        print("try again")
        main()

    else:
        print(f"{x}%")


def get_fuel():
    while True:
        try:
            fuel = input("fuel in fraction form x/y: ")
            x, y = map(int, fuel.split("/"))

            x = int(x)
            y = int(y)

            fuel_perc = (x / y) * 100
            roundedfuel = round(fuel_perc)

            return int(roundedfuel)
        except (ValueError, ZeroDivisionError):
            print("fuel is not an integer")


if __name__ == "__main__":
    main()
