while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    
    if a == b == c:
        print("Equilateral")
    elif max(a, b, c) >= a + b + c - max(a, b, c):
        print("Invalid")
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        print("Isosceles")
    else:
        print("Scalene")