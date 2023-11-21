def solution(arr):
    arr.append("*")
    answer = []
    idx = 0
    compare_num = arr[idx]
    
    for i in arr:
        # print(f'현재 i: {i}, 비교 숫자: {compare_num}')
        if i == compare_num:
            idx += 1
            # print(f'인덱스 증가')
        else:
            # print(f'숫자 {compare_num} 추가')
            answer.append(compare_num)
            compare_num = arr[idx]
            idx += 1
    
    return answer