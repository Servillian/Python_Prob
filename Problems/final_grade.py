import csv
import sys

try:
    filename = sys.argv[-1]
    file = open(filename)
except:
    print("file not found, exiting program")
    exit()

class Student:
    # LN = Last Name, FN = Final name
    def __init__(self, LN, FN, ID, test):
        self.LN = LN
        self.FN = FN
        self.ID = ID
        self.test = test

reader = csv.reader(file)
header = next(reader)
last_name = ""
first_name = ""
student_id = ""
a = ""; b = ""; c = ""; d = ""

for row in reader:
    last_name += row[0] + ", "
    first_name += row[1] + ", "
    student_id += row[2] + ", "
    a += row[3] + ", "; b += row[4] + ", "; c += row[5] + ", "; d += row[6] + ", "

last = last_name.split(",")
first = first_name.split(",")
id = student_id.split(",")
t1 = a.split(","); t2 = b.split(","); t3 = c.split(","); t4 = d.split(",")




def av(tests):
    return (int(tests[0]) + int(tests[1]) + int(tests[2]) + int(tests[3]))/4


def tg(average):
    if average > 90:
        return "A+"
    elif average > 80:
        return "A"
    elif average > 75:
        return "B+"
    elif average > 70:
        return "B"
    elif average > 65:
        return "C+"
    elif average > 60:
        return "C"
    elif average > 55:
        return "D+"
    elif average >= 50:
        return "D"
    elif average < 50:
        return "F"


l1 = t1[0], t2[0], t3[0], t4[0]
l2 = t1[1], t2[1], t3[1], t4[1]
l3 = t1[2], t2[2], t3[2], t4[2]
l4 = t1[3], t2[3], t3[3], t4[3]
l5 = t1[4], t2[4], t3[4], t4[4]
l6 = t1[5], t2[5], t3[5], t4[5]
l7 = t1[6], t2[6], t3[6], t4[6]
l8 = t1[7], t2[7], t3[7], t4[7]
l9 = t1[8], t2[8], t3[8], t4[8]
l10 = t1[9], t2[9], t3[9], t4[9]
l11 = t1[10], t2[10], t3[10], t4[10]
l12 = t1[11], t2[11], t3[11], t4[11]
l13 = t1[12], t2[12], t3[12], t4[12]
l14 = t1[13], t2[13], t3[13], t4[13]
l15 = t1[14], t2[14], t3[14], t4[14]
l16 = t1[15], t2[15], t3[15], t4[15]


FinalGrade1 = tg(av(l1))
FinalGrade2 = tg(av(l2))
FinalGrade3 = tg(av(l3))
FinalGrade4 = tg(av(l4))
FinalGrade5 = tg(av(l5))
FinalGrade6 = tg(av(l6))
FinalGrade7 = tg(av(l7))
FinalGrade8 = tg(av(l8))
FinalGrade9 = tg(av(l9))
FinalGrade10 = tg(av(l10))
FinalGrade11 = tg(av(l11))
FinalGrade12 = tg(av(l12))
FinalGrade13 = tg(av(l13))
FinalGrade14 = tg(av(l14))
FinalGrade15 = tg(av(l15))
FinalGrade16 = tg(av(l16))


Student1 = Student(first[0], last[0], id[0], av(l1))
print(Student1.FN, Student1.LN, Student1.ID, Student1.test, FinalGrade1)
Student2 = Student(first[1].strip(), last[1].strip(), id[1].strip(), av(l2))
print(Student2.FN, Student2.LN, Student2.ID, Student2.test, FinalGrade2)
Student3 = Student(first[2].strip(), last[2].strip(), id[2].strip(), av(l3))
print(Student3.FN, Student3.LN, Student3.ID, Student3.test, FinalGrade3)
Student4 = Student(first[3].strip(), last[3].strip(), id[3].strip(), av(l4))
print(Student4.FN, Student4.LN, Student4.ID, Student4.test, FinalGrade4)
Student5 = Student(first[4].strip(), last[4].strip(), id[4].strip(), av(l5))
print(Student5.FN, Student5.LN, Student5.ID, Student5.test, FinalGrade5)
Student6 = Student(first[5].strip(), last[5].strip(), id[5].strip(), av(l6))
print(Student6.FN, Student6.LN, Student6.ID, Student6.test, FinalGrade6)
Student7 = Student(first[6].strip(), last[6].strip(), id[6].strip(), av(l7))
print(Student7.FN, Student7.LN, Student7.ID, Student7.test, FinalGrade7)
Student8 = Student(first[7].strip(), last[7].strip(), id[7].strip(), av(l8))
print(Student8.FN, Student8.LN, Student8.ID, Student8.test, FinalGrade8)
Student9 = Student(first[8].strip(), last[8].strip(), id[8].strip(), av(l9))
print(Student9.FN, Student9.LN, Student9.ID, Student9.test, FinalGrade9)
Student10 = Student(first[9].strip(), last[9].strip(), id[9].strip(), av(l10))
print(Student10.FN, Student10.LN, Student10.ID, Student10.test, FinalGrade10)
Student11 = Student(first[10].strip(), last[10].strip(), id[10].strip(), av(l11))
print(Student11.FN, Student11.LN, Student11.ID, Student11.test, FinalGrade11)
Student12 = Student(first[11].strip(), last[11].strip(), id[11].strip(), av(l12))
print(Student12.FN, Student12.LN, Student12.ID, Student12.test, FinalGrade12)
Student13 = Student(first[12].strip(), last[12].strip(), id[12].strip(), av(l13))
print(Student13.FN, Student13.LN, Student13.ID, Student13.test, FinalGrade13)
Student14 = Student(first[13].strip(), last[13].strip(), id[13].strip(), av(l14))
print(Student14.FN, Student14.LN, Student14.ID, Student14.test, FinalGrade14)
Student15 = Student(first[14].strip(), last[14].strip(), id[14].strip(), av(l15))
print(Student15.FN, Student15.LN, Student15.ID, Student15.test, FinalGrade15)
Student16 = Student(first[15].strip(), last[15].strip(), id[15].strip(), av(l16))
print(Student16.FN, Student16.LN, Student16.ID, Student16.test, FinalGrade16)
