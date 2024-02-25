def main():
    dict = {
        "apple": 130,
        "avocado": 50,
        "sweet cherries": 100,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "tangerine": 50,
        "watermelon": 80,
    }

    fruit = input("pick a fruit: ").lower()
    if fruit in dict:
        print(f"Calories: {dict[fruit]}")


main()
