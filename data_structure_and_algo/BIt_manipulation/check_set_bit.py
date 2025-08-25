def checkKthBit(n, k): 
    MaskedBit = 1 << k 
    if n & MaskedBit :
        return True
    
    return False

def checkKthBit2(n, k): 
    if (n >> k) & 1  == 1:
        return True
    
    return False

print(checkKthBit2(7, 3))