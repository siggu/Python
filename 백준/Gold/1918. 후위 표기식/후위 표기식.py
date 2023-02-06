infix_expr = input()

prec = {}
prec["*"] = 3
prec["/"] = 3
prec["+"] = 2
prec["-"] = 2
prec["("] = 1

stack = []
postfix_list = []
token_list = []
for i in infix_expr:
    token_list.append(i)

for token in token_list:
    if token not in '()*/+-':
        postfix_list.append(token)
    elif token == "(":
        stack.append(token)
    elif token == ")":
        top_token = stack.pop()
        while top_token != "(":
            postfix_list.append(top_token)
            top_token = stack.pop()
    else:
        while (not len(stack) == 0) and (prec[stack[-1]] >= prec[token]):
            postfix_list.append(stack.pop())
        stack.append(token)

while not len(stack) == 0:
    postfix_list.append(stack.pop())

print(''.join(postfix_list))