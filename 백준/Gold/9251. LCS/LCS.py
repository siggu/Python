word1 = input()
word2 = input()
len1 = len(word1)
len2 = len(word2)

lcs = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if word1[i-1] == word2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[-1][-1])