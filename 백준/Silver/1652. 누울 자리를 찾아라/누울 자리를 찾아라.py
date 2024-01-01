N = int(input())
_list = [list(map(str, input())) for _ in range(N)]

row = 0
column = 0

for i in range(N):
    len_row, len_column = 0, 0
    for j in range(N):
        if _list[i][j] == ".":
            len_row += 1
        else:
            len_row = 0
        if len_row == 2:
            row += 1

        if _list[j][i] == ".":
            len_column += 1
        else:
            len_column = 0
        if len_column == 2:
            column += 1

print(row, column)