def linear_search(arr , target) :

    result = -1

    for num in arr :
        if num == target :
            result = num
    
    return result

arr = [1 , 2 , 3 , 4 ,5]
print(linear_search(arr,7))