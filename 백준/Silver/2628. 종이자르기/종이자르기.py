width, height = map(int, input().split())
n = int(input())
heights = [0, height]
widths = [0, width]

for _ in range(n):
    a, b = map(int, input().split())
    if a:
        widths.append(b)
    else:
        heights.append(b)

widths.sort()
heights.sort()
result = 0

for i in range(len(widths) - 1):
    for j in range(len(heights) - 1):
        result = max(
            result, (heights[j + 1] - heights[j]) * (widths[i + 1] - widths[i])
        )

print(result)