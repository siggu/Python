def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    cnt = 0
    
    while True:
        try:
            if participant[cnt] == completion[cnt]:
                cnt += 1
            else:
                return participant[cnt]
        except:
            return participant[-1]