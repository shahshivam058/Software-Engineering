"""
array greter element then it self 

for each element in array check if greter element available or not 
greter element greter element current element in array 


Brute force approch :

brute force approch we can use is 

for each element we can count the element greter then it self we cant sort the array it might affect the count 

Loop over the array for each element 
for each element run nested loop from i + 1 to n 

count that 

optimal approch 

findout the maximum number 
count all the element less then max 
and return the result

"""

def greter_then_number(arr) :
    result = 0 
    largest_element = max(arr) 

    for num in arr :
        if num < largest_element:
            result += 1
    
    return result

arr= [1 , 2 ,3 , 4 ,5]
print(greter_then_number(arr))