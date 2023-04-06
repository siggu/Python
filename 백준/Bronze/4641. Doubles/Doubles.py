while True:
    nums = list(map(int, input().split()))
    cnt = 0
    
    if len(nums) == 1:
        exit()
    
    for j in nums:
        if j*2 in nums:
            cnt += 1
            continue

    print(cnt-1)