def solution(s):
    s = s.split(" ")
    result = []
    
    for i in s:
        word = ""
        
        for idx, alphabet in enumerate(i):
            if idx % 2 == 0:
                word += alphabet.upper()
            else:
                word += alphabet.lower()
    
        result.append(word)

    return ' '.join(result)
    

    return result