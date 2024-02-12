ans = input("say 42 ")

match ans:
    case "42" | "Fourty Two" | "fourty-two":
        print("yes")
    case _:
        print("no")
