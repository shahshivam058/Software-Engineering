def total_sum(arr) :
    result = 0

    for index in range(len(arr)):
        result = result + arr[index]

    return result

arr = [5 , 2 , 7, 9 , 10 ]

print(total_sum(arr))