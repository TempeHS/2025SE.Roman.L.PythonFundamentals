def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    f2 = s[:2]
    l1 = s[-1]
    punc = [".", ",", "!", "?", " ", ":", ";"]

    if not 2 <= len(s) <= 6:
        return False

    if not f2.isalnum():
        return False

    if l1.isdigit() == 0:
        return False

    if any(char in (punc) for char in s):
        return False

    for char in s:
        if char.isdigit():
            if not char == "0" and s[-1].isdigit():
                return True
            else:
                return False

    return True


main()
