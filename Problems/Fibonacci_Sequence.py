d = {}
def fibonacci(n):
    if n in d:
        return d[n]
    value = 0
    if n <= 2:
        return 1
    else:
        value = fibonacci(n-1)+ fibonacci(n-2)
        d[n] = value
        return value


for i in range(60):
    print(fibonacci(i))
# print(fibonacci(20))