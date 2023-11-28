from collections import deque

def solution(cacheSize, cities):
    hit = 0
    miss = 0
    cities_lower = []
    for i in cities:
        cities_lower.append(i.lower())
    lru_cache = deque()
    
    for i in cities_lower:
        if cacheSize == 0:
            return len(cities_lower)*5
        if cacheSize > len(lru_cache):
            if i in lru_cache:
                lru_cache.remove(i)
                lru_cache.appendleft(i)
                hit += 1
            elif i not in lru_cache:
                lru_cache.appendleft(i)
                miss += 1
        elif cacheSize <= len(lru_cache):
            if i in lru_cache:
                lru_cache.remove(i)
                lru_cache.appendleft(i)
                hit += 1
            elif i not in lru_cache:
                lru_cache.pop()
                lru_cache.appendleft(i)
                miss += 1
        
        # print(f'데이터 가져온 후 캐시 = {lru_cache}')
        
    return (hit*1 + miss*5)