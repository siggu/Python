def solution(record):
    result = []
    log = {}
    
    for i in record:
        info = i.split()
        
        if info[0] == "Leave":
            continue
        
        log[info[1]] = info[2]

    for i in record:
        info = i.split()
        
        if info[0] == "Enter":
            result.append(f"{log[info[1]]}님이 들어왔습니다.")
        elif info[0] == "Leave":
            result.append(f"{log[info[1]]}님이 나갔습니다.")
    
    return result