x, y, w, h = map(int, input().split())
min_dot = []

min_dot.append(w-x)
min_dot.append(h-y)
min_dot.append(x)
min_dot.append(y)

print(min(min_dot))