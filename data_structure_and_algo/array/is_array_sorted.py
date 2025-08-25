def check_if_array_sorted(arr) :

    for index in range(len(arr) - 1) :
        if arr[index] > arr[index + 1]:
            return False
    
    return True


arr = [1 , 2 , 3 ,4 , 3]
print(check_if_array_sorted(arr))


def is_sorted_ascending(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1)) if len(arr) > 1 else True