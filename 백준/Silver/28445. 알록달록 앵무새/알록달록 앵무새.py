colors = set()

for _ in range(2):
    parents = input().split()
    for p in parents:
        colors.add(p)

sorted_colors = sorted(list(colors))

for i in sorted_colors:
    for j in sorted_colors:
        print(i, j)