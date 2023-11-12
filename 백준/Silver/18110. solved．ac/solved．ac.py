from sys import stdin
input = stdin.readline

def round45(num) :
    return int(num) + [0, 1][num - int(num) >= 0.5]

n = int(input())
if n == 0 : print(0)
else :
    nums = sorted([int(input()) for _ in range(n)])
    temp = round45(n * 0.15)
    if temp > 0 : nums = nums[temp : -temp]
    print(round45( sum(nums) / (n - temp*2) ))