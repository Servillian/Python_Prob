string = "a a b b b c c "
l = string.split()
d = {}
for i in l:
    if i not in d:
        d[i] = 1
    elif i in d:
        d[i] += 1

print(d)