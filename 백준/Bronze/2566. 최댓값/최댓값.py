table = [list(map(int, input().split())) for _ in range(9)]

max_value = -1
max_row = -1
max_col = -1

for i in range(9):
    for j in range(9):
        if table[i][j] > max_value:
            max_value = table[i][j]
            max_row = i + 1
            max_col = j + 1

print(max_value)
print(max_row, max_col)