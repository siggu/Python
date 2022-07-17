V = int(input())
vote = input()
vote_list = []
A_num = 0
B_num = 0

for x in vote:
    vote_list.append(x)

for y in vote_list:
    if y == 'A':
        A_num += 1
    else:
        B_num += 1

if A_num > B_num:
    print('A')
elif A_num < B_num:
    print('B')
else:
    print('Tie')