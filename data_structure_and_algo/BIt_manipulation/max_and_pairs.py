

def max_and_pais(arr) :
    result = 0 
    candidates = arr.copy()

    for bit_pos in range(31,-1,-1):
        number_with_bits = []
        for number in candidates :
            if (number >> bit_pos) & 1 == 1 :
                number_with_bits.append(number)
        
        if len(number_with_bits) >= 2 :
            result = result | (1 << bit_pos)
            candidates = number_with_bits
        
    return result


# Start from MSB (bit 31) down to LSB (bit 0)
# For each bit position: Count how many numbers have this bit set to 1
# If ≥2 numbers have the bit set: Include this bit in the result and keep only those numbers for next iteration
# If <2 numbers have the bit set: Skip this bit (can't form a pair with both having this bit)


        

test_cases = [
        [3, 10, 5, 25, 2, 8],
        [1, 2, 3, 4, 5],
        [8, 4, 2, 1],
        [15, 7, 31, 63],
        [1, 3, 5, 7, 9],
        [16, 17, 18, 19],
        [100, 200, 300]
]

for i in test_cases :
    print(max_and_pais(i))