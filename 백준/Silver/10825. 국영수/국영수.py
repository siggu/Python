n = int(input())
student = []

for _ in range(n):
    name, x, y, z = list(map(str, input().split()))
    student.append([name, int(x), int(y), int(z)])

student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in student:
    print(i[0])