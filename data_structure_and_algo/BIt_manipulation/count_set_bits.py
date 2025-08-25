
def count_set_bits(number) : 
    count = 0 

    while number :
        if  number & 1 == 1 :
            count = count + 1
        number = number >> 1 
    
    return count

def count_set_bits_2(number) : 
    count = 0 

    while number :
        count = count + 1
        number = number & (number - 1) 
    
    return count


print(count_set_bits_2(7))
print(count_set_bits_2(10))