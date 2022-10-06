import sys
read = sys.stdin.readline

board = read().rstrip()
result = []
cnt = 0

while True:
    if board[cnt:cnt+4] == 'XXXX':
        result.append('AAAA')
        cnt = cnt + 4
        if cnt == len(board):
            break    
    elif board[cnt:cnt+2] == 'XX':
        result.append('BB')
        cnt = cnt + 2
        if cnt == len(board):            
            break    
    elif board[cnt] == '.':
        result.append('.')
        cnt += 1
        if cnt == len(board):            
            break
    else:
        print(-1)
        exit()

for i in result:
    print(i,end='')