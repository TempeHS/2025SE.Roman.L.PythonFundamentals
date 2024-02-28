def main():

    months = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12,
    }

    while True:
        date = input("date in month day and year: ").lower()

        if "/" in date:
            try:
                m, d, y = date.split("/")
                m, d, y = int(m), int(d), int(y)

                if m > 12:
                    True

                else:
                    print(f"{y}-{m:02}-{d:02}")
                    return

            except ValueError:
                True

        for alfred in months:
            if alfred in date:
                try:
                    m, d, y = date.split(" ")
                    d = d.replace(",", "")
                    d, y = int(d), int(y)
                    m = months[alfred]

                    if d > 31:
                        True
                    else:

                        print(f"{y}-{m:02}-{d:02}")
                        return

                except ValueError:
                    True


main()
