p1, p2, p3 = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))

ccw = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1]) # ccw(Counter Clock Wise) 알고리즘

if ccw > 0:
    print(1)
elif ccw < 0:
    print(-1)
else:
    print(0)