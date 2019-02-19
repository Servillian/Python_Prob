a = int(input("Enter the month(1-12): \n"))

if (a >= 3) and (a<= 5):
    print("It's autumn. Enjoy the beautiful sunsets!")
elif (a >= 6) and (a<= 8):
    print("It's winter, go skiing!")
elif (a >= 9) and (a<= 11):
    print("It's spring. Check out the spring racing carnival!")
elif (a== 12) or (a<3 and a >0):
    print("It's summer. Have fun in the sun!")
else:
    print("Invalid input. Please enter any number between 1 and 12")
