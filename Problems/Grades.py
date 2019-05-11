import csv

file = open("grades.csv.csv")

reader = csv.reader(file)
header = next(reader)

def stringtoint(test):
    lst = []
    for i in test:
        lst.append(int(i))
    return lst
def grade(final):
    if final > 90:
        return "A+"
Student1 = next(reader)

# for student in reader:
lastname1 = Student1[0]
firstname1 = Student1[1]
studentnumber1 = int(Student1[2])
# testscores1 = [Student1[3], Student1[4], Student1[5], Student1[6]]
testscores1 = Student1[3:]
testscores1 = stringtoint(testscores1)
finalGrade = sum(testscores1)/len(testscores1)


print(testscores1)
print(finalGrade)
