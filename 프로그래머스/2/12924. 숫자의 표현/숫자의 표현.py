def solution(n):
    cnt = 0 # 표현 방법
    for i in range(1, n+1):
        # print(f'{i} 시작')
        temp = i
        result = i
        while result < n:
            temp += 1
            result += temp
            if result == n:
                # print(f'{i}에서 추가')
                cnt += 1
    
    return cnt+1
            