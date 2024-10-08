n = int(input())
user = set()
result = 0

for i in range(n):
    chat = input()    
    if chat == "ENTER":
        result += len(user)
        # print(f'result = {result}, user = {user}')
        user = set()
    else:
        user.add(chat)

result += len(user)
print(result)