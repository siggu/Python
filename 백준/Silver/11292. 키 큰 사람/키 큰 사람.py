while True:
    t = int(input())
    
    if t == 0:
        break

    names = []
    heights = []
    
    for _ in range(t):
        name, height = map(str, input().split())
        names.append(name)
        heights.append(height)
    
    max_height = max(heights)
    result = []
    
    for i in range(len(heights)):
        if heights[i] == max_height:
            result.append(names[i])
    
    print(" ".join(result))