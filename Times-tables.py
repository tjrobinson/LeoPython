table = int(input("Please enter a times table:"))
something = "yuhgfghg"
while something != "detryukjhggfd":
        for x in range(0,13):
            if table < 13:
                print(x, "x", table, "=", x*table)
            else:
                print("The times table was too high.")
                table = int(input("Please enter a times table: "))
                something = "hghjkgtfhbv"