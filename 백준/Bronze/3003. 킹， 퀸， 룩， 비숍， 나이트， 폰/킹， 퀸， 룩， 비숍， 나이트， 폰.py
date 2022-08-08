found_piece = list(map(int, input().split()))
piece = [1, 1, 2, 2, 2, 8]
count = 0

for x in found_piece:
    print(piece[count] - x,end=' ')
    count += 1