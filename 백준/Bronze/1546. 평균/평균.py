N = int(input())
score_list = list(map(int, input().split()))
new_score = 0

M = max(score_list)

for x in score_list:
    x = x / M * 100
    new_score += x
    
print(new_score / len(score_list))