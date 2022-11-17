import sys
read = sys.stdin.readline

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

T = int(read())

for _ in range(T):
    n = int(read())
    
    while True:
        if is_prime(n):
            print(n)
            break
        else:
            n += 1