# percentage rounded to the nearest integer


def main():
    x = get_fuel()
    print(f"fuel is {x}")


def get_fuel():
    try:
        fuel = int(input("fuel in fraction form x/y: "))
        x, y = fuel.split("/")

        x = int(x)
        y = int(y)

        fuel = (x / y) * 100
        return int(fuel)
    except (ValueError, ZeroDivisionError):
        print("fuel is not an integer")


if __name__ == "__main__":
    main()
