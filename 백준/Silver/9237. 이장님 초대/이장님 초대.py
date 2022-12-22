n = int(input())
t = list(map(int, input().split()))

t.sort(reverse=True)
arr = []

for i in range(n):
    arr.append(t[i] + 1 + i)

print(max(arr)+1)