import sys
N = int(sys.stdin.readline())

arr = []

for _ in range(N):
    name = sys.stdin.readline().rstrip()
    arr.append(name)

increase = list(arr)
increase.sort()

decrease = list(arr)
decrease.sort(reverse=True)

if arr == increase:
    print('INCREASING')
elif arr == decrease:
    print('DECREASING')
else:
    print('NEITHER')