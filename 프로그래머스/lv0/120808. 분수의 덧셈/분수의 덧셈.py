def gcd(n, m):
    while n % m != 0:
        n, m = m, n % m
    return m

def solution(denum1, num1, denum2, num2):
    num3 = gcd(num1, num2)
    denum3 = num1 * num2 // num3
    mole = denum1 * (num2 // num3) + denum2 * (num1 // num3)
    
    num4 = gcd(denum3, mole)
    return [mole//num4, denum3//num4]