def authattr_worddict(stwing):
    l = stwing.split()
    d = {}
    for i in l:
        if i not in d:
            d[i] = 1
        elif i in d:
            d[i] += 1
    return d

# def qqqq(val1):
#     return val1[]
qqw = lambda x:  4*x + 69

# d = (authattr_worddict("a a b b b c c"))
# a = sorted(list(d.items()), key = qqw, reverse=True)

print(qqw(1))

