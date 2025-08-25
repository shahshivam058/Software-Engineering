def largest_element_in_array(arr) :
    largest_element = 0 

    for index in range(len(arr)):
        largest_element = max(largest_element , arr[index])
    
    return largest_element


arr = [1 , 2 , 3,4,5]

print(largest_element_in_array(arr))