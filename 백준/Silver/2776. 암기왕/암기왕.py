import sys
read = sys.stdin.readline
t = int(read())

for _ in range(t):
    n = int(read())
    s1 = set(map(int, read().rstrip().split()))
    
    m = int(read())
    s2 = list(map(int, read().rstrip().split()))
    
    for i in s2:
        if i in s1:
            print(1)
        else:
            print(0)