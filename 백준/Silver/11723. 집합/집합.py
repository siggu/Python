import sys
read = sys.stdin.readline

S = set()
M = int(read())

for _ in range(M):
    cal = read().strip().split()

    if len(cal) == 1:
        if cal[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        func, num = cal[0], cal[1]
        num = int(num)

        if func == "add":
            S.add(num)
        elif func == "remove":
            S.discard(num)
        elif func == "check":
            if num in S:
                print(1)
            else:
                print(0)
        elif func == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)
