import sys
read = sys.stdin.readline

time = 0

for _ in range(4):
    time += int(read())

print(time // 60)
print(time % 60)