triangles = [int(input()) for _ in range(3)]

if sum(triangles) == 180:
    if triangles[0] == triangles[1] == triangles[2]:
        print("Equilateral")
    elif triangles[0] == triangles[1] or triangles[1] == triangles[2] or triangles[0] == triangles[2]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")