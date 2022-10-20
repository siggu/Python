import sys
read = sys.stdin.readline

def mean(arr):
    return round(sum(arr) / len(arr))

def median(arr):
    arr.sort()
    return arr[int(len(arr) / 2)]

def mode(arr):
    dic = {}
    num_list = []
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 0
    
    dic = sorted(dic.items(), key=lambda x:x[1])
    dic = dict(dic)
    max_num = [k for k,v in dic.items() if max(dic.values()) == v]

    if len(max_num) >= 2:
        max_num.sort()
        return max_num[1]
    else:
        return max_num[0]

def list_range(arr):
    arr.sort()
    return arr[-1] - arr[0]

N = int(read())
arr = []

for _ in range(N):
    num = int(read())
    arr.append(num)

print(mean(arr))
print(median(arr))
print(mode(arr))
print(list_range(arr))