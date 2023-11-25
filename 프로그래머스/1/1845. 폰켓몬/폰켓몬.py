def solution(nums):
    set_nums = list(set(nums))
    
    if len(set_nums) >= len(nums) / 2:
        return len(nums) / 2
    elif len(set_nums) < len(nums):
        return len(set_nums)