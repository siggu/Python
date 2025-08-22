g, p, t = map(int, input().split())

# g = 그룹의 수, p = 각 그룹의 사람 수, t = 양성 반응을 보인 그룹의 수
individual = g * p
test_in_group = g + (p * t)

if individual < test_in_group:
    print(1)
elif individual > test_in_group:
    print(2)
else:
    print(0)