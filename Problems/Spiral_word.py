def spiral_word(word):
    #Checking no duplicates
    if len(set(word)) != len(word):
        return False
    a = -1
    result = list(word[0])
    for i in range(1,len(word)//2+1):
        result.append(word[i*a])
        if i == len(word)//2:
            break
        result.append(word[i])
    return result == sorted(result, reverse=True) or result == sorted(result, reverse=False)


print(spiral_word("all"))
