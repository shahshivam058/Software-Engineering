def PrimeNumber(n):
    """
        Number N is said to be Prime if Number is Divisible 1 and it self 
        Here We are Looping From 2 to n-1
        if number is divisible by number between 2 to n - 1 then non prime else prime
    """
    for i in range(2,n):
        if n % i == 0 :
            print("Not a Prime Number")
            return
    
    print("Prime Number")


def PrimeNumber2(n):
    """
        Number N is said to be Prime if Number is Divisible 1 and it self 
        Hence Prime Number only have two factors 1 and another is it self
        so for prime number there will be only 2 factors 
        so Looping from 1 to n 
        if and checking number only has two factor then prime else non prime
    """
    count = 0
    for i in range(1,n+1):
        if n % i == 0 :
            count = count + 1
    
    if count == 2:
        print("Prime Number")
    else:
        print("Not a Prime Number")

from math import isqrt
def PrimeNumber3(n):
    """
        Number N is said to be Prime if Number is Divisible 1 and it self 
        Hence Prime Number only have two factors 1 and another is it self
        At any point we will have all unique factors till sqrt of n 
        so just need to loop till sqrt of n 
    """
    IsPrime = True
    for i in range(2,isqrt(n)+1):
        if n % i == 0 :
            IsPrime = False
            break
    
    if IsPrime:
        print("Prime Number")
    else:
        print("Not a Prime Number")

def PrimeNumber4(n):
    """
        Number N is said to be Prime if Number is Divisible 1 and it self 
        Hence Prime Number only have two factors 1 and another is it self
        At any point we will have all unique factors till sqrt of n 
        so just need to loop till sqrt of n 
    """
    isPrime = True
    i = 2
    while i*i <= n :
        if n % i == 0 :
            isPrime = False
            break
            
        i += 1
    
    if isPrime:
        print("Prime Number")
    else:
        print("Not a Prime Number")



PrimeNumber3(3)
PrimeNumber3(4)
PrimeNumber3(5)
PrimeNumber3(7)

