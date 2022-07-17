N = int(input())
print_list = []
count = 0

for _ in range(N):
    r, e, c = map(int, input().split())
    
    if (e - c) > r:
        print_list.append('advertise')
    elif (e -c) < r:
        print_list.append('do not advertise')
    else:
        print_list.append('does not matter')

for _ in range(N):
    print(print_list[count])
    count += 1