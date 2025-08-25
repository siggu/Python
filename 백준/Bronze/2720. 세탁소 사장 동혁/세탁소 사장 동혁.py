# 쿼터: 0.25, 다임: 0.1, 니켈: 0.05, 페니: 0.01

T = int(input())

for _ in range(T):
    C = int(input())
    result = []
    
    for i in range(4):
        result.append(C // [25, 10, 5, 1][i])
        C %= [25, 10, 5, 1][i]
        
    print(*result)