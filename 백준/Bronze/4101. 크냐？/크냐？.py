answer_list = []
count = 0

while True:
    x, y = map(int, input().split())
    if x > y:
        answer_list.append('Yes')
    elif x == 0 and y == 0:
        break
    elif x <= y:
        answer_list.append('No')

for _ in answer_list:
    print(answer_list[count])
    count += 1