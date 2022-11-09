def solution(n):
    pizza = 6
    while True:
        if pizza % n == 0:
            return pizza // 6
        else:
            pizza += 6