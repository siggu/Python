import sys

score_arr = []
final_arr = []

result = 0

for _ in range(8):
    score = int(sys.stdin.readline())

    score_arr.append(score)

for _ in range(5):
    final_arr.append(score_arr.index(max(score_arr))+1)

    result += max(score_arr)

    score_arr[score_arr.index(max(score_arr))] = -1

final_arr.sort()
print(result)

for x in final_arr:
    print(x,end=' ')