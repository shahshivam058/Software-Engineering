"""
The problem asks for the number of contiguous non-empty subarrays where the maximum element is within a given range [left, right]. We can solve this by using the principle of inclusion-exclusion.

The number of subarrays with a maximum element in the range [left, right] is equal to:
(Number of subarrays with a maximum element 
le right) - (Number of subarrays with a maximum element 
le left - 1).

To implement this, we can create a helper function that counts all subarrays where the maximum element is less than or equal to a given value k.

Helper Function: count_subarrays_with_max_le(arr, k)
This function iterates through the input array arr and keeps track of the length of the current contiguous sequence of numbers that are 
le k. For each number num in the array:

If num is less than or equal to k, it extends the current valid sequence. The number of new subarrays that end at the current position is equal to the length of this extended sequence. We add this to our total count.

If num is greater than k, it breaks the sequence, so we reset the current count to zero.

The total count accumulated is the number of subarrays with a maximum element 
le k.

Final Calculation
Call the helper function with right as the limit: count_le_right = count_subarrays_with_max_le(nums, right). This gives us the total count of subarrays where the maximum value is at most right.

Call the helper function with left - 1 as the limit: count_lt_left = count_subarrays_with_max_le(nums, left - 1). This gives us the total count of subarrays where the maximum value is strictly less than left.

The final result is the difference between these two counts: count_le_right - count_lt_left.

This method is efficient with a time complexity of O(n) because we perform a single pass over the array for each call to the helper function.



The Principle of Inclusion-Exclusion
The problem asks us to count subarrays where the maximum element M satisfies left <= M <= right. This is a specific range. It's often easier to count things that are less than or equal to a certain value.

The principle of inclusion-exclusion allows us to find the count within a range [L, R] by calculating:

(Count of items with value ≤ R) - (Count of items with value < L)

Think of it like this:

You have a large bag of all the subarrays where the maximum element is at most right (i.e., max <= right). This bag includes all the subarrays you want, but it also contains some you don't want—specifically, those whose maximum element is less than left.

You have a second, smaller bag of all the subarrays where the maximum element is strictly less than left (i.e., max <= left - 1).

To get exactly what you want, you simply remove the second bag from the first.

This method avoids the complexity of trying to handle three different cases for each element in the array (< left, [left, right], > right) in a single pass, which can be prone to errors. It simplifies the problem by breaking it into two passes, each with a single, clear condition.



"""

"""
So The problem is number of subarrays with bounded maximum 

given a array a of size n with left and right return the count of subarrays in such way maximum number in subarray is between left and right 

max number in subarray should be in range of left and right 

brute force approch 

genrate all of subarray anc check if maximum in subarray in range of left to right if max in range just increase the count 


TC (N ** 2) * O(N)


think each index one by one as endpoint for each inded we have to identify valid starting point




when arr[endpoint] > R
        valid starting point will be 0 no metter where we start we will include which is greter than right and make ans 0 

when arr[endpoint] >= l and arr[endpoint] <= R
      from current point go to left and if number in a range will be in valid range and it can be starting point 

      when we reach number which is not in range then it can not be a good starting point 


      valid starting point will be from  [last greter index element + 1 ,endpoint ]
      within range we have all counts are the valid index 
      we can count of number
      if number is not in range l to r we cant add that not a valid 
      ep- lgie + 1 = valid counts 

when arr[endpoint] < L
    IT WILL BE NOT GOING INTO RANGE
    When number is in range  then only it can be greter then endpoint  startpoint can be first number which can be in range

    
Valid starting point = number of valid starting point for the element[L , R] just before the current element 


for (ep = 0 ,ep < n , ep++)
if arr[ep] > r :
    ans += 0
    lsgi = ep+1

else arr[ep] < r and arr[ep] > L
        ans = ans + (ep - lsgi + 1)
    prevcount = (ep - lsgi + 1) no of valid starting point 

else arr[ep] < L:
    ans = ans + prevcount 
"""