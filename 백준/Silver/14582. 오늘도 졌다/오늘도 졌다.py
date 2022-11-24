import sys
read = sys.stdin.readline

J = list(map(int, read().rstrip().split()))
G = list(map(int, read().rstrip().split()))
J_cnt = 0
G_cnt = 0

for i in range(9):
    J_cnt += int(J[i])
    
    if J_cnt > G_cnt:
        print("Yes")
        break
    elif i == 8 and J_cnt <= G_cnt:
        print("No")
    G_cnt += int(G[i])