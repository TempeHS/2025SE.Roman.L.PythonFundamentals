def main():
    return input("write face: ")


def convert(face):
    face = face.replace(":)", "🙂")
    face = face.replace(":(", "🙁")
    return face


faceinput = main()
print(convert(faceinput))
