def check_move(column, row):
    assert(type(column) == str)
    if column in "ABCDEFGH" and row in range(9) and type(column) != bool and type(row) != bool:
        print(f"This piece is moved to {column}{row}")
    else:
        print("Not Valid")
    return
