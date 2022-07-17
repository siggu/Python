bowl = input()
bowl_list = []
height = 10
    
for x in bowl:
    bowl_list.append(x)
        
count = 0 

for _ in range(len(bowl_list)-1):
    if bowl_list[count] == bowl_list[count+1]:
        height += 5
    else:
        height += 10
    count += 1

print(height)