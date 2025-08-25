def single_number_2(arr) :
    xor_sum = 0 

    for number in arr :
        xor_sum = xor_sum ^ number
    
    bit_pos = xor_sum & ~xor_sum

    unique_number_1 = 0 
    unique_number_2 = 0 

    for number in arr :
        if (number >> bit_pos) & 1  == 1 :
            unique_number_1 =  unique_number_1 ^ number
        else :
            unique_number_2 = unique_number_2 ^ number

    return unique_number_1 , unique_number_2

arr = [1,1,2,2,3,3,4,4,5,6,7,7,8,8,9,9]

single_number_2(arr)

