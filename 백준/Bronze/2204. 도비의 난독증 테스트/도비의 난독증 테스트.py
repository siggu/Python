while True:
    n = int(input())

    if n == 0:
        break
    
    compare = []
    
    for _ in range(n):
        compare.append(input())
    
    compare.sort(key=str.lower)
    
    print(compare[0])