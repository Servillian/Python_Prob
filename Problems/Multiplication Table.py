num = int(input("Enter the number for 'num': "))
N = int(input("Enter the number for 'N': "))
for i in range(1, N+1):
    if (num > 0) and (N > 0):
        print(i, "*", num, "=", num*i)
