presidents = ["Franklin", "Grant", "Jackson", "Hamilton", "Lincoln", "Washington"]
bills = [100, 50, 20, 10, 5, 1]
n = int(input())

for _ in range(n):
    result = 0
    president = list(map(str, input().split()))
    
    for i in president:
        result += bills[presidents.index(i)]
    
    print(f'${result}')