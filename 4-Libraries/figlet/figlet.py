import sys
from pyfiglet import Figlet

figlet = Figlet()


def main():

    try:
        if "-f" in (sys.argv[1]) and (sys.argv[2]) in figlet.getFonts():
            stuff = input("")
            print(Figlet(sys.argv[2]).renderText(stuff))

        else:
            print("Invalid Usage")
            sys.exit

    except IndexError:
        print("Invalid Usage")
        sys.exit


main()
