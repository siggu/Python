A = int(input())
B = int(input())
C = int(input())

count = 0
num_list = []

cal = A * B * C
cal = str(cal)
cal_list = []

for x in cal:
    cal_list.append(x)


for x in range(10):
    count = 0
    for y in cal_list:
        if x == int(y):
            count += 1
    num_list.append(count)
    
 
for x in num_list:
    print(x)