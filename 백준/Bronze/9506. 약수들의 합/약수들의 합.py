print_list = []
count = 1
sum = 0

while True:
    aList = []
    n = int(input())
    
    if n == -1:
        break
        
    for x in range(n):
        if count == n:
            break
        if n % count == 0:
            aList.append(count)
        count += 1

    for x in aList:
      sum += x
    
    if sum == n:
        print(f'{n} = ',end='')
        for x in range(len(aList)):
            print(f'{aList[x]} ',end='')
            if x == len(aList) - 1:
                print()
                break
            else:
                print('+ ', end='')
    else:
      print(f'{n} is NOT perfect.')

    sum = 0
    count = 1