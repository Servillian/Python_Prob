pi = input("How much money would you like to invest: \n")
time = input("How many days would you like to invest this for: \n")
a = int(pi)
b = int(time)
r = 4.5/100
n = int(b//30)
pf = a *(1+ r/12)**n
print(pf)