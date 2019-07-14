a = [1,2,3]
def search(lst,element):
    for i in lst:
        if i == element:
            return True
    return False




print(search(a,3))
