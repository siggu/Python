n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

cnt = 0
first = 0
last = n - 1
while first < last:
    mid = nums[first] + nums[last]
    
    if mid == x:
        cnt += 1
        first += 1
    elif mid < x:
        first += 1
    else:
        last -= 1

print(cnt)