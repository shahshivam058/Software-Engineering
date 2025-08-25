def reversal_part_of_array(arr , start, end) :
    while start <= end :
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1
    
    return arr

arr = [1 , 2,3,4,5,6,7,8,9,0]
print(reversal_part_of_array(arr , 3 , 8))
