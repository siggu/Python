def solution(s):
    answer = 0
    arr = []
    s = list(map(str, s.split()))

    for i in s:
        arr.append(i)
        if i =='Z':
            arr.pop()
            if len(arr) >= 1:
                arr.pop()
    for i in arr:
        answer += int(i)
    return answer