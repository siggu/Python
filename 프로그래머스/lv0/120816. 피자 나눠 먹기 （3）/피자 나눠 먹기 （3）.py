def solution(slice, n):
    cnt = 0
    while True:
        if n <= slice:
            return cnt+1
        else:
            n -= slice
            cnt += 1