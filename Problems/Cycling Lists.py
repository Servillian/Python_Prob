def cycle(input_list):
    c = input_list[1:] + input_list[:1]
    return c


print(cycle("45d12"))
