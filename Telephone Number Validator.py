num = input("Enter your phone number: ")
a = num[0]
if len(num) == 8:
    if int(a) <= 0:
        print("ERROR: Invalid Input")
else:
    print("ERROR: Invalid Input")

