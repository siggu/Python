import sys
read = sys.stdin.readline

a, b = map(int, read().rstrip().split())
set_A = set(map(int, read().rstrip().split()))
set_B = set(map(int, read().rstrip().split()))

difference = set_A - set_B
difference = list(difference)
difference.sort()

print(len(difference))
for x in difference:
    print(x,end=' ')