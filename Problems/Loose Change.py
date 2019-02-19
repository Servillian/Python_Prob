while True:
    a = input("How much did it cost: \n")
    b = int(a[-1])

    if (b>0 and b<=2) or (b>5 and b<7):
        print("Cash")
    elif (b>2 and b<=5) or (b>7 and b<=9):
        print("Card")