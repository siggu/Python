import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
listen_list = set()
see_list = set()

for _ in range(N):
    name = sys.stdin.readline().rstrip()
    listen_list.add(name)

for _ in range(M):
    name = sys.stdin.readline().rstrip()
    see_list.add(name)

see_listen = sorted(list(listen_list & see_list))

print(len(see_listen))

for x in see_listen:
    print(x)