n, m = map(int, input().split())
brands = [list(map(int, input().split())) for _ in range(m)]
package = []
each = []
result = []

for i in range(m):
    package.append(brands[i][0])
    each.append(brands[i][1])

min_package = min(package)
min_each = min(each)

if min_package > min_each * 6:
    print(min_each * n)
else:
    if (n % 6) * min_each < min_package:
        print((n // 6) * min_package + (n % 6) * min_each)
    else:
        print((n // 6 + 1) * min_package)