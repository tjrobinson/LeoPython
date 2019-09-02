import random
for x in range(1):
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
    print("Today for breakfast eat",food,)
    nothing = input("Press enter to play again.")