t = int(input())

for _ in range(t):
    num = str(input())
    
    result = int(num) + int(num[::-1])
    
    if str(result) == str(result)[::-1]:
        print('YES')
    else:
        print("NO")