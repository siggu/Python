num = list(map(int, input().split()))
double = 0

for x in num:
    double += x**2
    
print(double % 10)