def solution(s):
    cnt_same = 0
    cnt_diff = 0
    idx_left = 0
    idx_right = 0
    x = s[0]
    result = []
    
    for i in range(len(s)):
        if s[i] == x:
            cnt_same += 1
        elif s[i] != x:
            cnt_diff += 1
        # print(f'현재 s[i]값: {s[i]}, 현재 x값: {x} cnt_same: {cnt_same}, cnt_diff: {cnt_diff}')
        if cnt_same == cnt_diff:
            result.append(s[idx_left:idx_left + cnt_same + cnt_diff])
            idx_left += cnt_same + cnt_diff
            # print(f'idx_left = {idx_left}')
            try:
                x = s[idx_left]
            except:
                pass
            cnt_same = 0
            cnt_diff = 0
        elif cnt_same != cnt_diff:
            if i == len(s)-1:
                result.append(s[idx_left:idx_left + cnt_same + cnt_diff])
            else:
                pass
    
    return len(result)