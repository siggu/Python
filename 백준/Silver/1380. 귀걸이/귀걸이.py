cnt = 1
result = []

while True:
    n = int(input())
    in_out = []
    num_sum = 0

    if n == 0:
        break
    
    name = [input() for _ in range(n)]

    for i in range(2*n - 1):
        in_out.append(list(map(str, input().split()))[0])

    in_out.sort()

    for i in in_out:
        if in_out.count(i) == 1:
            result.append(name[int(i)-1])
    
for i in result:
    print(cnt, i)
    cnt += 1