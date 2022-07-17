N = int(input())
one_num = 0
zero_num = 0

for _ in range(N):
    vote = int(input())
    
    if vote == 1:
        one_num += 1
    else:
        zero_num += 1

if one_num > zero_num:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')