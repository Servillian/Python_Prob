def check_move(placement):
    column = placement[0]
    row = int(placement[1])

    if column.upper() in "ABCDEFGH":
        if row in range(1,9):
            print(f"This piece is moved to {column.upper()}{row}")
        else:
            print("The row value is not in range 1 to 8!")
    else:
        print("Not Valid")
    return
