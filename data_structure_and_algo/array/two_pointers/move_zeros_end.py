"""
The Two-Pointer Approach
The core idea is to use one pointer to track the position where the next non-zero element should be placed and another to iterate through the array. This effectively partitions the array into two sections: a non-zero section at the beginning and a zero section at the end.

Initialize Pointers:

write_pointer (or last_non_zero_found_at): This pointer starts at index 0 and tracks the position where the next non-zero element should be written. Think of it as the "write head" of the non-zero section.

read_pointer (or current): This pointer also starts at index 0 and iterates through the entire array, checking each element. Think of it as the "read head."

Iterate and Swap/Overwrite:

Iterate with the read_pointer from the beginning to the end of the array.

At each step, check the value at array[read_pointer].

If the element is non-zero: This is an element we want to keep. We move it to the position pointed to by the write_pointer.

If the read_pointer and write_pointer are at the same location, there's no need to swap; we simply increment both.

If they are at different locations, it means we have encountered one or more zeros that the write_pointer has skipped over. We swap the non-zero element with the element at the write_pointer's position.

After moving the non-zero element, we increment the write_pointer to make room for the next non-zero element.

If the element is zero: We simply do nothing with the write_pointer and continue iterating with the read_pointer. The write_pointer remains in place, waiting for the next non-zero element.

Completion:

After the read_pointer has finished iterating through the entire array, all non-zero elements will be at the beginning of the array in their original relative order.

The write_pointer will be at the first position where a zero should be placed.

The remaining elements from the write_pointer to the end of the array will already be zeroes (due to the swaps or because they were never overwritten). There is no need for a separate pass to fill them with zeroes.



"""



def moveZeroes(nums):
    """
    Moves all zeroes in an array to the end while maintaining the relative
    order of the non-zero elements.

    This function uses a two-pointer approach to perform the operation in-place.
    One pointer ('write_pointer') tracks where the next non-zero element should be
    placed, and the other pointer ('read_pointer') iterates through the array.

    Args:
        nums (list[int]): The list of numbers to be modified.
    """
    # The 'write_pointer' tracks the position to place the next non-zero element.
    write_pointer = 0

    # The 'read_pointer' iterates through the array to find non-zero elements.
    for read_pointer in range(len(nums)):
        # If the element at the 'read_pointer' is non-zero,
        # we move it to the position of the 'write_pointer'.
        if nums[read_pointer] != 0:
            # Check if the pointers are at the same position. This avoids
            # unnecessary swaps when the array starts with non-zero numbers.
            if read_pointer != write_pointer:
                # Swap the non-zero element with the element at the
                # 'write_pointer' position.
                nums[write_pointer], nums[read_pointer] = nums[read_pointer], nums[write_pointer]
            
            # Increment the 'write_pointer' to prepare for the next non-zero element.
            write_pointer += 1
