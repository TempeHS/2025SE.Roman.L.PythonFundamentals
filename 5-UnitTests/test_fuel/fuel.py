def main():
    while True:
        fuel = input("fuel in fraction form x/y: ")
        percentage = convert(fuel)
        if percentage is not None:
            gauge(percentage)
            break


def convert(fraction):
    while True:
        try:
            x, y = map(int, fraction.split("/"))

            x = int(x)
            y = int(y)

            fuel_perc = (x / y) * 100
            fraction = round(fuel_perc)

            if fraction > 100 or fraction < 0:
                print("try again")
                return None

            else:
                return fraction

        except (ValueError, ZeroDivisionError):
            print("fuel is not an integer")
            return None


def gauge(percentage):
    if 0 <= int(percentage) <= 1:
        print("E")
        return "E"

    elif 99 <= int(percentage) <= 100:
        print("F")
        return "F"

    else:
        print(f"{percentage}%")
        return percentage


if __name__ == "__main__":
    main()
