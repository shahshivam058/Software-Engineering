"""
https://leetcode.com/problems/number-of-senior-citizens/description/

You are given a 0-indexed array of strings details. Each element of details provides information about a given passenger compressed into a string of length 15. The system is such that:

array consist of information each information decoded into 15 length string 
where 
The first ten characters consist of the phone number of passengers. 0 - 9
The next character denotes the gender of the person. 10
The following two characters are used to indicate the age of the person. 11 - 12 
The last two characters determine the seat allotted to that person. 13 and 14 
Return the number of passengers who are strictly more than 60 years old.

we are just checking number of encoded information which has age more than 60 

simplest opretion we can just use slicing opretion 


"""


class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        
        result = 0 

        for info in details :
            age = int(info[11:13]) # we are extracting age and convert to integers 
            # ord() gives the ASCII value of a character.
            #Subtracting ord("0") converts a character digit like '7' into the integer 7.

            """
            integer     ascii 
            0           48
            1           49
            2           50 

            we only have ascii for 0 to 9 digits 
            more than 1 length  string digit  we cant convert to ascii it will throng the error so we can convert the string digits group int digit by digit 
            to get the actual digit for each number we can use ascii of 0 
            we can subtract ascii of digit with ascii of 0 we can get actual digit 
              
            """


            # ten = ord(d[11]) - ord("0") 
            # one = ord(d[12]) - ord("0")
            # age = one + 10 * ten # extract both digit individually and convert it to int using assci  and then use this formula 

            if age > 60 :
                result = result + 1
            
        return result 
