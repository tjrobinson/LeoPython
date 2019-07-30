import random
while True:
    foods = ["toast","toast","cereal","cereal","cat food"]
    food = random.choice(foods)
    if food == "cat food":
        catfoods = ["kitten food","cat food"]
        food = random.choice(catfoods)
        if food == "kitten food":
            kittenfoods = ["dry kitten food","wet kitten food"]
            food = random.choice(kittenfoods)
    elif food == "toast":
        toppings = ["toast with nuttela","toast with marmite","toast with nuttela","toast with marmite","toast with wet kitten food","kitten food sandwidge with bread"]
        food = random.choice(toppings)
    to choose again nothing = input("Press enter.")
    print("Today for breakfast eat",food,)