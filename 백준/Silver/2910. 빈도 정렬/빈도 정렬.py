from collections import Counter

n, c = map(int, input().split())
arr = list(map(int, input().split()))

result = Counter(arr).most_common()

for i,j in result:
    for _ in range(j):
        print(i, end=' ')