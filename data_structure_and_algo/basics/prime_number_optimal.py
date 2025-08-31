import math 

def prime_number(n) :
    if n <= 1 :
        return False
    
    if n <= 3 :
        return True
    
    if n % 2 == 0 or n % 3 == 0 or i % 5 == 0  :
       return False

    check_till_n = int(math.sqrt(n)) + 1
    for i in range(2 , check_till_n) :
        if n % i == 0 :
            return False
    
    return True  

    # another logic for prime number 
    # i = 2 

    # while  i * i <= n :
    #     if n % i == 0 :
    #         return False
    #     i = i + 1
    
    # return True
    

for i in range(1 , 100) :
    print(i ,"is" , prime_number(i)) 


def prime_number(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    final_number = int(math.sqrt(n)) + 1
    for i in range(5, final_number, 2):  # check only odd numbers
        if n % i == 0:
            return False
    return True
"""
1. Even numbers > 2 are never prime

- Example: 4, 6, 8, 10, ...
- They’re always divisible by 2.
- Since you already handled n % 2 == 0 earlier in the code, you never need to check even divisors again.
- So in the loop, checking i = 4, 6, 8, ... is pointless — they’ll never divide a prime number.

2. Why odd numbers are enough

- If a number n has a factor, at least one factor will be ≤ √n.
- Suppose you’re testing n = 37.
- √37 ≈ 6, so you only need to check divisors up to 6.
- Possible divisors: 2, 3, 4, 5, 6.
- You already ruled out 2 and 3 before the loop.
- 4 is even (no need to test again).
- So only 5 remains → 37 % 5 ≠ 0 → 37 is prime ✅.
"""