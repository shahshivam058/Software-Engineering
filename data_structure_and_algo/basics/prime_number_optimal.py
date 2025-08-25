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
