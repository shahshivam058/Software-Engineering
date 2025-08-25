def xor_queries(arr, queries):
    # Step 1: Build the prefix XOR array
    prefix = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix[i] = prefix[i - 1] ^ arr[i - 1]

    # Step 2: Answer each query using prefix XOR
    result = []
    for L, R in queries:
        xor_value = prefix[R + 1] ^ prefix[L] # Subtract the contribution of Prefix from prefix[R + 1] which gives anwser between l and r 
        result.append(xor_value)

    return result

# Example usage
arr = [1, 3, 4, 8]
queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
output = xor_queries(arr, queries)
print(output)  # Output: [1^3=2, 3^4=7, 1^3^4^8=14, 8]
