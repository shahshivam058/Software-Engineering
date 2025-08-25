def single_number_2(arr) :
    result = 0 

    for bit_pos in range(32) :
        count_bits = 0 
        for number in arr :
            if (number >> bit_pos) & 1 == 1 :
                count_bits  = count_bits + 1
        
        if count_bits % 3 == 1 :
            result = result | (1 << bit_pos)
    
    return result

arr = [1,1,1,2,2,2,3,3,3,4]

print(single_number_2(arr))


"""
each integer consist of 32 bit 
Loop over each bit position for each number in array of integers 
count number of set bit at particular bit posi and check if multiple of 3 or not
if not multiple of 3 then add that number to result 


(1 << bit_pos) = bit position where bit is not multiple of 3 we are just setting 1 at particular bit pos to form a anwser 


"""