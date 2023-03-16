import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    result = 1
    grade = []
    
    for i in range(n):
        grade.append(list(map(int, input().split())))

    grade.sort(key= lambda x: (x[0]))
    
    compare = grade[0][1]
    
    for i in range(n):
        if compare > grade[i][1]:
            result += 1
            compare = grade[i][1]
    
    print(result)