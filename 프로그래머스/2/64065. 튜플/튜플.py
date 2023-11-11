def solution(s):
    answer = []
    s = s[:-2].replace("{", "").replace(",", " ").split("}")
    
    for i, v in enumerate(s):
        s[i] = v.split()
    
    s.sort(key=lambda x:len(x))
    
    for i in s:
        for j in answer:
            i.remove(j)
        answer.append(i[0])
    
    return [int(i) for i in answer]