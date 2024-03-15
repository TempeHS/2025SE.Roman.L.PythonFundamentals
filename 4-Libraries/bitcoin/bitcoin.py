import sys
import requests

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice/USD.json")
data = r.json()


def main():
    try:
        inp = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        return
    except IndexError:
        print("Missing command-line argument")
        return

    try:
        btc_price = float(data["bpi"]["USD"]["rate"].replace(",", ""))
        want = inp * btc_price

        want = float(want)

        print(f"${want:,.4f}")

    except requests.RequestException:
        print("Failed to get Bitcoin price")
        return


if __name__ == "__main__":
    main()
