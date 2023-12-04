def solution(s):
    zero_cnt = 0
    trans_cnt = 0
    
    while s != "1":
        zero_cnt += s.count("0")
        s = s.replace("0", "")
        s = str(bin(len(s))[2:])
        trans_cnt += 1
    
    return [trans_cnt, zero_cnt]