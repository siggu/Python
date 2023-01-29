n, k, i = map(int, input().split())
count = 0

while k != i:
    k -= k // 2
    i -= i // 2
    count += 1
    
print(count)