n = int(input())
x_point = 0
y_point = 0

for _ in range(n):
    x, y = map(int, input().split())
    
    if x > y:
        y_point += x
    elif y > x:
        x_point += y
   
print(100 - x_point)
print(100 - y_point)