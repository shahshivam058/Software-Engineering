"""
You are given an encoded string s, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
There will not be input like 3a, 2[4], a[a] or a[2].

The test cases are generated so that the length of the output will never exceed 100,000.



Here's how to decode a string like 3[a2[c]]:

Algorithm
Initialize Stacks and Variables:

num_stack: A stack to store repeat counts (numbers).
str_stack: A stack to store decoded strings.
current_str: A string builder or variable to accumulate the current character sequence.
current_num: An integer variable to build the current number.


Iterate Through the String:
If the character is a digit:
Build the number by accumulating the digits. For example, if you see 1 and then 0, current_num becomes 10.




If the character is [:
Push the current_num onto num_stack.
Push the current_str onto str_stack.
Reset current_num to 0.
Reset current_str to an empty string. This prepares for decoding the content of the new brackets.


If the character is ]:
Pop the last number from num_stack. This is the repeat count.
Pop the last string from str_stack. This is the string from the previous level.
Repeat current_str by the number of times you just popped.
Append this repeated string to the string you just popped from str_stack.
Update current_str to this new, combined string.
If the character is a letter:
Append the character to current_str.


Final Result:

After the loop finishes, the current_str variable will hold the fully decoded string.

One possible way we can have nested brackates 
To Solve Outside problem we have to solve inside problem 
To solve whole problem we have to solve inner problem 
we may use recursion tree solve the problem 
we dont need to maintain anything 


for nested stack is really helpfull 
Go char by char from start to end 
when you found the digit add it to stack 
when opening breackate push to stack and go in left 
when found the closing brackate we gonna pop everysingle char from stack untill we found the opening brackate 
when found digit pop 



"""





class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)

        for i in range(n):
            if s[i] != ']':
                stack.append(s[i])
            else :
                substr = ""
                while stack[-1] != "[":
                    substr =  stack.pop() + substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                k = int(k)
                stack.append(k * substr)


        return "".join(stack) 
                
