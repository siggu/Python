import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
check_word = [read().rstrip() for _ in range(N)]
cnt = 0

for i in range(M):
    word = read().rstrip()
    if word in check_word:
        cnt += 1
    
print(cnt)