# Approach
# Understanding XOR Contribution by Bit Position:

# The XOR operation between two bits is 1 if the bits are different, and 0 if they are the same.

# For each bit position (0 to 31 for 32-bit integers), calculate how many pairs of numbers have different bits at that position. This count will determine the contribution of that bit to the total sum.

# Counting Set Bits:

# For each bit position i, count the numbers in the array where the i-th bit is set (1). Let this count be count.

# The numbers where the i-th bit is not set (0) will be n - count, where n is the total number of elements in the array.

# Calculating Pairs with Different Bits:

# The number of pairs where one number has the i-th bit set and the other doesn't is count * (n - count).

# Each such pair contributes 2^i to the total sum.

# Summing Contributions from All Bits:

# For each bit position, multiply the number of valid pairs by 2^i and accumulate this value across all bits to get the final sum.


def xor_all_sum(arr) :
    result = 0 
    n = len(arr) 
    for bit_pos in range(32):
        count = 0 
        for number in arr :
            if (number >> bit_pos ) & 1 == 1 :
                count = count + 1
        
        result += count * (n - count) * (1 << bit_pos)
    
    return result

arr = [1,2,3]
result = xor_all_sum(arr)
print(result)