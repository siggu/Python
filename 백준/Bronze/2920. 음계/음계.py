num = list(map(int, input().split()))

ascending = [1, 2, 3, 4, 5, 6, 7, 8]

if num == ascending:
    print("ascending")
elif num == ascending[::-1]:
    print("descending")
else:
    print("mixed")