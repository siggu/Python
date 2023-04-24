t = int(input())

for _ in range(t):
    num = input()
    cnt = 0
    
    while num != "6174":
        max_num = int(''.join(sorted(num, reverse=True)))
        min_num = int(''.join(sorted(num)))
        num = str(max_num - min_num)

        if len(num) < 4:
            idx = ""
            
            for i in range(4 - len(num)):
                idx += '0'
            num = idx + num
        
        cnt +=1 
    
    print(cnt)