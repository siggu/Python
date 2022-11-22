def solution(num, k):
    cnt = 1
    num = str(num)
    
    for i in num:
        if int(i) == k:
            return cnt
        if cnt == len(num):
            return -1
        cnt += 1