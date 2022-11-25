N = int(input())
stack = list(map(int, input().split()))
result = []
answer = [-1] * N

result.append(0)

for i in range(1, N):
    while result and stack[result[-1]] < stack[i]:
        answer[result.pop()] = stack[i]
    result.append(i)

print(*answer)