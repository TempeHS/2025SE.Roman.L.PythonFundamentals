def dollars_to_float(d):

    return float(d.replace("$", ""))


# its a fraction


def percentfl(p):
    return float(p.replace("%", "")) / 100


# shortened line 18 to avoid problem


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percentfl(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


main()
