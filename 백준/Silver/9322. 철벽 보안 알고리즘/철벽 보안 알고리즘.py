t = int(input())

for _ in range(t):
    n = int(input())
    
    
    one = list(map(str, input().split()))
    two = list(map(str, input().split()))
    code = list(map(str, input().split()))
    
    word = ["" for _ in range(n)]
    
    for i in range(len(one)):
        # word[i] = code[one.index(two[i])]
        # print(code[one.index(two[i])])
        # print(one.index(two[i]))
        word[one.index(two[i])] = code[i]

    print(*word)