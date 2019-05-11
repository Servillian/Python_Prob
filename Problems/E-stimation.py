def factorial(a):
    b = 1
    for i in range(1, a+1):
        b *= i
    return b


def e_estimator(n):
    c = 0
    for i in range(0, n+1):
        c += 1/factorial(i)
    return c

print(e_estimator(3))





