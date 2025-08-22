while True:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break
    
    carry_count = 0
    carry = 0
    
    while a > 0 or b > 0:
        a_digit = a % 10
        b_digit = b % 10
        
        if a_digit + b_digit + carry >= 10:
            carry_count += 1
            carry = 1
        else:
            carry = 0
        
        a //= 10
        b //= 10
    
    print(carry_count)