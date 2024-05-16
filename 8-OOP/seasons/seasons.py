from datetime import date
from num2words import num2words
import re
import sys


def main():
    try:
        bdate = input("YYYY-MM-DD: ")
        year, month, day = bdate.split("-")

    except ValueError:
        sys.exit("Invalid Date")

    dt = date(int(year), int(month), int(day))
    today = date.today()

    minus = today - dt

    calculation = minus.days * 24 * 60
    word_form = num2words(calculation)

    # removed and, excluding in thousand
    cleaned_word_form = re.sub(r"\b(?:and)\b", "", word_form)

    print(cleaned_word_form)


if __name__ == "__main__":
    main()
