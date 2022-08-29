x_list = []
y_list = []
for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

data = [x_list, y_list]

output = []
for i in data:
    count = 0
    tmp = i[0]
    i.remove(tmp)
    
    if tmp not in i:
        output.append(tmp)
        continue
        
    for j in i:
        if tmp != j:
            output.append(j)

print(output[0], output[1])