def single_number_1(arr) : 
    result = 0 
    for number in arr :
        result ^= number
    
    return result

arr = [1,1,2,2,3,4,4,5,5,6,6,7,7]

print(single_number_1(arr))