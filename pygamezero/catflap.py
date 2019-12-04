global fuzz
global jedi
global mr_baggins
global blaze

jedi = input("Is Jedi in or out?")
fuzz = input("Is Fuzz in or out?")
mr_baggins = input("Is Mr Baggins in or out?")
blaze = input("Is Blaze in or out?")

while True:

    thing = input("Has a cat come through?")
    if thing == "yes":
        cat = input("Who came through?")
        way = input("Which way?")
        if cat == "Fuzz":
            if way == "out":
                fuzz = "out"
            else:
                fuzz = "in"
        elif cat == "jedi":
            if way == "out":
                jedi = "out"
            else:
                jedi = "in"
        elif cat == "Mr Baggins":
            if way == "out":
                mr_baggins = "out"
            else:
                mr_baggins = "in"
        elif cat == "Blaze":
            if way == "out":
                blaze = "out"
            else:
                blaze = "in"
    elif thing == "no":
        thing2 = input("Do you want to see where the cats are?")
        if thing2 == "yes":
            print("Fuzz is", fuzz + "side")
            print("Jedi is", jedi + "side")
            print("Mr Baggins is", mr_baggins + "side")
            print("Blaze is", blaze + "side")