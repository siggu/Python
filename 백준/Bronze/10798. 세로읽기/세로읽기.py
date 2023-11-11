list = []
answer = ""
max_len = 0

for i in range(5):
    list.append(input())

for i in list:
    if len(i) > max_len:
        max_len = len(i)


for i in range(5):
    list[i] = list[i].ljust(max_len, "*")

for i in range(max_len):
    for j in list:
        answer += j[i]

answer = answer.replace("*", "")

print(answer)