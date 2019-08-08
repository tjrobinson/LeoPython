from random import randint
end_card = 11
while end_card > 10:
    score = 0
    game_over = False
    end_card = int(input("Enter a number from 1 to 10 to be your end card: "))
    while game_over == False:
        currentcard = randint(0,10)
        while currentcard != end_card:
            if end_card == 1:
                if currentcard == 2:
                    score = score + 1
                elif currentcard == 3:
                    score = score + 2
                elif currentcard == 4:
                    score = score + 3
                elif currentcard == 5:
                   score = score + 4
                elif currentcard == 6:
                    score = score + 5
                elif currentcard == 7:
                    score = score + 6
                elif currentcard == 8:
                   score = score + 7
                elif currentcard == 9:
                    score = score + 8
                elif currentcard == 10:
                    score = score + 9
            elif end_card == 2:
                if currentcard == 1:
                    score = score + 1
        print("Game over!")
        print("Your score was ",score)
        game_over = True



