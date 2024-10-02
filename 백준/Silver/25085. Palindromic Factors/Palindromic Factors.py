t = int(input())

def all_factors(n):
    result = set()
    
    for x in range(1, int(n**0.5) + 1):
        if n % x == 0:
            result |= {x, n // x}
    
    return result

def is_palindromes(m):
    m = str(m)

    if m != m[::-1]:
        return False
    
    return True


for i in range(t):
    a = int(input())
    answer = 0
    
    for j in all_factors(a):
        if is_palindromes(j):
            answer += 1
    
    print(f'Case #{i+1}: {answer}')