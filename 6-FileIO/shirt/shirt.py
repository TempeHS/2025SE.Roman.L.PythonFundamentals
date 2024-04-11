import sys
from PIL import Image


def main():
    try:
        image_extensions = (".png", ".jpg", ".jpeg")
        real1 = sys.argv[1].split(".")[-1].lower()
        real2 = sys.argv[2].split(".")[-1].lower()

        if len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit()

        elif real1 != real2:
            print("Not the same type")
            sys.exit()

        elif not sys.argv[1].endswith(image_extensions):
            print("Not a supported file")
            sys.exit()

        else:
            try:
                shirt = Image.open("took.png")
                bin = Image.open(sys.argv[1])
                shirt_width, shirt_height = shirt.size
                bin_width, bin_height = bin.size
                realshirt = shirt.resize((bin_width, bin_height))
                bin.paste(realshirt, (0, 700))
                bin.save(sys.argv[2])

            except FileNotFoundError:
                print("File not found")
                sys.exit()

    except IndexError:
        print("Too few command-line arguments")
        sys.exit()


if __name__ == "__main__":
    main()
