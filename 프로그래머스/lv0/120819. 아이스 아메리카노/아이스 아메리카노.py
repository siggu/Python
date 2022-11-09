def solution(money):
    cnt = 0
    while True:
        if money < 5500:
            return [cnt, money]
        else:
            money -= 5500
            cnt += 1