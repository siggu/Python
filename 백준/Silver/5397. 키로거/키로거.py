t = int(input())

for _ in range(t):
    password = input()
    s1 = []
    s2 = []

    for i in password:
        if i == ">":
            if s2:
                s1.append(s2.pop())
        elif i == "<":
            if s1:
                s2.append(s1.pop())
        elif i == "-":
            if s1:
                s1.pop()
        else:
            s1.append(i)
    
    print("".join(s1) + "".join(reversed(s2)))