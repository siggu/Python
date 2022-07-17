case_list = []
count = 0

while True:
    x, y = map(int, input().split())
    count += 1
    
    if x == 0 and y == 0:
        break
    
    if x % y == 0:
        case_list.append('multiple')
    elif y % x == 0:
        case_list.append('factor')
    else:
        case_list.append('neither')
    
   
for x in case_list:
    print(x)