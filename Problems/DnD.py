import random
def luck_tester(lucky_number,max_rolls,dice_size):
    for i in range(1, max_rolls):
        a = random.randint(1, dice_size)
        print(a)
        if a == lucky_number:
            return ["num of attempts", i]
    return False

print(luck_tester(5,5,10))