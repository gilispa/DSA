"""
Given a string s consisting of lowercase English Letters. return the first non-repeating character in s. If there is no non-repeating character, return '$'.
"""
class Solution:
    def nonRepeatingChar(self,s):
        #code here
        hash = {}
        
        for ele in s:
            if ele in hash:
                hash[ele] = hash[ele] + 1
            else:
                hash[ele] = 1
        
        for ele in s:
            if hash[ele] == 1:
                return ele
        
        return "$"
    