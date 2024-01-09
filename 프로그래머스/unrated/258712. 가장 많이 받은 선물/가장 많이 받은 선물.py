def solution(friends, gifts):
    gift_list = [[0]*len(friends) for _ in range(len(friends))]
    result = [0]*len(friends)
    for i in gifts:
        give, get = map(str, i.split())
        gift_list[friends.index(give)][friends.index(get)] += 1
        
    print(gift_list)

    
    for i in range(len(result)):
        for j in range(i+1, len(result)):
            # 둘이 주고받은 선물 수가 다를 때
            if gift_list[i][j] != gift_list[j][i]:
                # (i, j)가 더 많이 줬을 때
                if gift_list[i][j] > gift_list[j][i]:
                    # i가 하나 받음
                    result[i] += 1
                else:
                    # j가 하나 받음
                    result[j] += 1
            # 둘이 주고받은 선물 수가 같을 때 or 아예 없을 때
            elif gift_list[i][j] == gift_list[j][i] or gift_list[i][j] == gift_list[j][i] == 0:
                # 선물 지수를 확인해 더 큰 사람한테 받음
                get_gift1 = 0
                get_gift2 = 0
                
                for k in range(len(result)):
                    get_gift1 += gift_list[k][i]
                    get_gift2 += gift_list[k][j]
                
                # i가 선물지수 더 큼
                if sum(gift_list[i]) - get_gift1 > sum(gift_list[j]) - get_gift2:
                    result[i] += 1
                # j가 선물지수 더 큼
                elif sum(gift_list[i]) - get_gift1 < sum(gift_list[j]) - get_gift2:
                    result[j] += 1
                # i와 j의 선물지수 같음
                elif sum(gift_list[i]) - get_gift1 == sum(gift_list[j]) - get_gift2:
                    pass
    
    return max(result)