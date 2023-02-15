n = int(input())
result = []
word = []
num = ""

for _ in range(n):
    word.append(input())

for i in word:
    for j in i:
        try:
            # print(f'j = {j}, int(j) = {int(j)}, num = {num}')
            if j == '0':
                num += '0'
            if int(j):
                num += j
        except:
            if num != "":
                if int(num) == 0:
                    result.append(0)
                    num = ""
                else:
                    result.append(int(num))
                    num = ""
    if num != "":
        if int(num) == 0:
            result.append(0)
            num = ""
        else:
            result.append(int(num))
            num = ""

result.sort()

for i in result:
    print(i)