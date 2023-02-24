while (n:=input())!='end':
    word_count=[0]*3
    flag=True
    
    for i in range(len(n)):
        if n[i] in 'aeiou':
            word_count[2]=0
            word_count[0]+=1
            word_count[1]+=1
        else:
            word_count[1]=0
            word_count[2]+=1
            
        if i<len(n)-1:
            if n[i]==n[i+1]:
                if n[i]=='e' or n[i]=='o':
                    pass
                else:
                    flag=False
                    break
                    
        if word_count[1]==3 or word_count[2]==3: 
            flag=False
            break
            
    if word_count[0]==0 or flag is False:
        print(f'<{n}> is not acceptable.')
    else:
        print(f'<{n}> is acceptable.')