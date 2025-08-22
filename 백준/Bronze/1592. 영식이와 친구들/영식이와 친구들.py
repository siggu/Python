N, M, L = map(int, input().split())

r = [0] * N
p = c = 0

while True:
    r[p] += 1
    if r[p] == M: break
    p = (p + L if r[p] % 2 else p - L) % N
    c += 1
    
print(c)