def factorial(a):
    b = 1
    for i in range(1, a+1):
        b *= i
    return b


def factorialRec(a):
    if a == 0:
        return 1
    return factorialRec(a-1)*a


print(factorialRec(3))