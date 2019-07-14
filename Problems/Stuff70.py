def bubble(lst):
    for i in range(len(lst)):
        # print(lst)
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

print(__name__)
if __name__ == "__main__":
    print("qwertyui")
# a = [7,3,4,1,59,84,37,7347,839,9,2,0]
# print(bubble(a))