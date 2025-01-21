nested_lst = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]


for outer_lst in nested_lst:
    print(f"Outer List: {outer_lst}")
    for num in outer_lst:
        print(f"Inner Element: {num}")