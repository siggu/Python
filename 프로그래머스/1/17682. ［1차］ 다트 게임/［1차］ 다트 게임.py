def solution(dartResult):
    
    num_list = []
    cnt = 0
    num = ""
    idx_left = 0
    idx_right = 0
    
    option = ["*", "#"]
    bonus = ["S", "D", "T"]
    
    
    for i in range(len(dartResult)-1):
        idx_right += 1
        if dartResult[idx_right] in bonus:
            num += dartResult[idx_left:idx_right]
            if dartResult[idx_right] == "S":
                num_list.append(int(num))
                idx_left = idx_right + 1
                cnt += 1
                num = ""
            if dartResult[idx_right] == "D":
                num_list.append(int(num)**2)
                idx_left = idx_right + 1
                cnt += 1
                num = ""            
            if dartResult[idx_right] == "T":
                num_list.append(int(num)**3)
                idx_left = idx_right + 1
                cnt += 1
                num = ""
        elif dartResult[idx_right] in option:
            idx_left += 1
            if dartResult[idx_right] == "*":
                if cnt == 1:
                    num_list[0] = num_list[0] * 2
                elif cnt == 2:
                    num_list[0] = num_list[0] * 2
                    num_list[1] = num_list[1] * 2
                elif cnt == 3:
                    num_list[1] = num_list[1] * 2
                    num_list[2] = num_list[2] * 2
            else:
                num_list[cnt-1] = num_list[cnt-1] * (-1)
        
    return sum(num_list)