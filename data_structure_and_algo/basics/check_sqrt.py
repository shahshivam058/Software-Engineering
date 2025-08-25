
def check_sqrt(n) :
    if n < 0 :
        return False # handling edge case as negative number can not have square 
    
    low = 0 
    high = n 

    while low <= high :
        mid = (low + high) // 2

        if mid * mid == n :
            return True
        elif mid * mid < n :
            low = mid + 1
        else :
            high = mid - 1
    
    return False