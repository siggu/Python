import sys
n = int(sys.stdin.readline())

in_out = set()
for _ in range(n):
    person, enter_leave = map(str, sys.stdin.readline().split())
    
    if enter_leave == 'enter':
        in_out.add(person)
    elif enter_leave == 'leave':
        in_out.remove(person)

in_out = list(in_out)
in_out.sort(reverse=True)

for x in in_out:
    print(x)