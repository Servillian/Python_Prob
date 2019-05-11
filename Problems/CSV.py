# import csv
file = open("Test.txt", "r")

print(file)

a = file.readlines()
print(a)
file.close()
for line in a:
    print(line)