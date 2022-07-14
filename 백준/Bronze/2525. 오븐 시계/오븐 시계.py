a,b=map(int,input().split())
c=int(input())
if (b+c)>59:
    a=a+(b+c)//60
    b=(b+c)%60
    if a>23:
        a=a%24
else:
    b=b+c
print(a,b)