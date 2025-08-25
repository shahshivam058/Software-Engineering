class Solution:
    def majorityElement(self, nums):
        Candidate = None 
        count = 0 

        for num in nums :
            if count == 0 :
                count += 1
                Candidate = num
            elif Candidate == num :
                count += 1
            else :
                count -= 1
        
        return Candidate
    

class Solution:
    def majorityElementTwo(self, nums):
        Candidate1 = None
        Candidate2 = None
        Count1  = 0 
        Count2 = 0 

        for num in nums :
            if num == Candidate1 :
                Count1 += 1
            elif num == Candidate2 :
                Count2 += 1
            elif Count1 == 0 :
                Candidate1 = num
                Count1 = 1
            elif Count2 == 0 :
                Candidate2 = num
                Count2 = 1
            else :
                Count1 -= 1
                Count2 -= 1
        
        Count1 = Count2 = 0 

        for num in nums :
            if num == Candidate1 :
                Count1 += 1
            elif Candidate2 == num :
                Count2 += 1
        
        result = []
        n = len(nums)
        if Count1 > n // 3:
            result.append(Candidate1)
        if Count2 > n // 3 :
            if Candidate1 != Candidate2 :
                result.append(Candidate2)
        
        return result
        
