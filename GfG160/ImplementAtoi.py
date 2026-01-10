"""
Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.

Cases for atoi() conversion:

Skip any leading whitespaces.
Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231.
"""

class Solution:
    def myAtoi(self, s):
        # Code here
        idx = 0
        n = len(s)
        sign = 1
        r = 0
        r_max = 2 ** 31 - 1
        r_min = -2 ** 31
        
        while idx < n and s[idx] == " ":
            idx += 1
        
        if idx < n and (s[idx] == "+" or s[idx] == "-"):
            if s[idx] == "-":
                sign = -1
            idx += 1
        
        while idx < n and "0" <= s[idx] <= "9":
            digit = ord(s[idx]) - ord("0")
            r = r * 10 + digit
            
        
            if sign * r > r_max:
                return r_max
                
            if sign * r < r_min:
                return r_min
                
            idx += 1
        
        return sign * r
        