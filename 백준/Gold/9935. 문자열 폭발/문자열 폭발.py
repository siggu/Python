import sys
input = sys.stdin.readline

word = list(input().rstrip())
delete = list(input().rstrip())
stack = []

for i in word:
    stack.append(i)
    if stack[-1] == delete[-1] and len(stack) >= len(delete):
        if stack[-len(delete):] == delete:
            for j in range(len(delete)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')