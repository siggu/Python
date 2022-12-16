# 0 : 0 1번, 1 0번
# 1 : 0 0번, 1 1번
# 2 : 1 + 0 -> 0 1번, 1 1번
# 3 : 2 + 1 -> 0 1번, 1 2번
# 4 : 3 + 2 -> 0 2번, 1 3번
t = int(input())

zero = [1, 0, 1]
one= [0, 1, 1]

def fibonacci(n):
    length = len(zero)

    if n >= length:
        for i in range(length, n + 1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(f'{zero[n]} {one[n]}')

for _ in range(t):
    fibonacci(int(input()))