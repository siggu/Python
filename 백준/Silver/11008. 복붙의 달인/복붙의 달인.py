n = int(input())

for _ in range(n):
    s, q = map(str, input().split())
    cnt = 0
    
    cnt = s.count(q)
    
    result = s.replace(q, "")
    print(cnt + len(result))