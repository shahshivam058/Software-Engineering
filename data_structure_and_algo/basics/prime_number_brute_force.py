
def prime_number(n) :
    if n <= 1 :
        return False
    # if n == 2 or n == 3 :
    #     return True

    if n <= 3 : # good check for  2 and 3 as 1 will be detected by above conditions  
        return True 
    
    if n % 2 == 0 or n % 3 == 0: # as 2 and 3 are really comman factors we can directly eliminate any number divisible by 2 or 3 
        return False

    
    count = 0 
    for i in range(1,n+1) :
        if n % i == 0 :
            count = count + 1
        
    
    if count == 2 :
        return True
    else :
        return False



# for i in range(1 , 100) :
#     print(i ,"is" , prime_number(i))


def prime_number2(n) :
    if n <= 1 :
        return False
    
    if n <= 3 :
        return True
    
    if n % 2 == 0 or n % 3 == 0 :
        return False
    
    for i in range(2,n):
        if n % i == 0 :
            return False
    
    return True

for i in range(1 , 100) :
    print(i ,"is" , prime_number2(i)) 
