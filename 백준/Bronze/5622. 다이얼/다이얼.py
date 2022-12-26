x = input()
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
cnt = 0
for i in range(len(x)):
    for j in dial:
        if x[i] in j:
            cnt += dial.index(j)+3
print(cnt)