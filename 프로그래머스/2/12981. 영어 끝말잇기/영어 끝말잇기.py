def solution(n, words):
    """
    1. 앞 사람이 말한 단어의 마지막 문자로 시작해야 함
    2. 쓴 단어 못 씀
    3. 한 글자 안됨
    """
    stack = []
    
    for i in range(0, len(words), n):
        stack.append(words[i:i+n])
    
    word = stack[0][0][0]
    check = []
    
    for i in stack:
        # print(f'현재 턴 = {i}')
        for j in i:
            # print(check)
            # print(f'{j}를 이미 말했는가? {j in check}')
            if j in check or j[0] != word or len(j) == 1:
                return [i.index(j)+1, stack.index(i)+1]
            word = j[-1]
            check.append(j)
        # print('---------------------')
    
    return [0, 0]