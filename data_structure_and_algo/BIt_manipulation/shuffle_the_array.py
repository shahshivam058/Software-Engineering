"""
Array can be of size n
array will of size 2 * n 
n /2  values are x 
n / 2 values are y 

currently all x values are stored to gather and all y values are storing togather 
store in x ,y group 

for the first elements x store the value i + n value 
store like first value from x first value from y 
x1,y1,x2,y2,x3,y3 and etc

max value we can store 1000 

combine the value of both x and y 

shift value of x by 10 after 10 th bit it will store value of x and from lsb to 10 bit it store the value of y 

        for i in range(n):
            nums[i] = (nums[i] << 10) | nums[i + n]  # Store x, y in nums[i]

            
extracr the value of both x and y

for y do and  opretion with bunch of 1 it will cancell out the x create 32 bit int and do and with number returns x which is arr[j]
now shift by 10 posi for correct location 

start doing from reverse loop end of array 
do 

"""


class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        for i in range(n) :
            nums[i] = (nums[i] << 10 ) | nums[i + n] # nums[i] store both the value value at the nums[i] and nums[i + n] first 10 bits from lsb will be n + i and after that i 
        
        j = 2 * n - 1 # total size of array 
        for i in range(n - 1 , -1 , -1) : # loop from end of array to 0
            y = nums[i] & ((1 << 10 )  - 1) # extract the y 
            x = nums[i] >> 10 # extract value x by shift 10 location means correct posityion 
            nums[j] = y # place at j location 
            nums[j - 1] = x # place at x
            j = j - 2
        
        return nums
        