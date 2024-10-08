n = int(input())
meet_chong = set(['ChongChong'])
people = set()

for _ in range(n):
    p1, p2 = input().split()
    
    if p1 == "ChongChong":
        if p2 in meet_chong:
            pass
        else:
            meet_chong.add(p2)
    elif p2 == "ChongChong":
        if p1 in meet_chong:
            pass
        else:
            meet_chong.add(p1)
    elif p1 and p2 != "ChongChong":
        if p1 in meet_chong:
            meet_chong.add(p2)
        elif p2 in meet_chong:
            meet_chong.add(p1)
    
    # print(f'p1={p1}, p2={p2}, 현재 총총이를 만난 사람들={meet_chong}')

print(len(meet_chong))