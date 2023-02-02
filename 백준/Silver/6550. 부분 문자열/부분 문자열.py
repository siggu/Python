while True:
    try:
        s, t = input().split()
        idx = 0
        word = ""
        
        for i in range(len(t)):
            if t[i] == s[idx]:
                word += t[i]
                idx += 1
                if idx == len(s):
                    break
        
        if s == word:
            print('Yes')
        else:
            print('No')
                 
    except:
        break