# breakfast 7-8, lunch 12-13, dinner 18-19


def main():
    x = input("what the time?: ")
    h, m = x.split(":")
    h = float(h)
    m = float(m)
    answer = convert(h, m)
    return answer


def convert(h, m):
    total = h + m / 60
    return total


if __name__ == "__main__":
    answer = main()

if 7 <= answer <= 8:
    print("breakfast time")

elif 12 <= answer <= 13:
    print("lunch time")

elif 18 <= answer <= 19:
    print("dinner time")

else:
    print("nothing")
