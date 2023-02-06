def solution(s):
    answer = ""
    stack = []
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in s:
        try:
            if int(i):
                answer += i
            elif i == "0":
                answer += "0"
        except:
            stack.append(str(i))
            join = ''.join(stack)
            if join in word:
                answer += str(word.index(join))
                stack = []
                
    return int(answer)