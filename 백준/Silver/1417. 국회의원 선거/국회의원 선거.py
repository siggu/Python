n = int(input())
dasom = int(input())
votes = []
cnt = 0

for i in range(n-1):
    vote = int(input())
    votes.append(vote)

if n != 1:
    while dasom <= max(votes):
        dasom += 1
        cnt += 1
        votes[votes.index(max(votes))] -= 1

print(cnt)