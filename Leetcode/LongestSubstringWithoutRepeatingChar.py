"""
Given a string s, find the length of the longest substring without duplicate characters.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        left = 0
        right = 0
        maxlen = 0

        for right in range(len(s)):
            while s[right] in hash:
                hash.pop(s[left])
                left += 1
            
            hash[s[right]] = right
            maxlen = max(maxlen, right - left + 1)

        return maxlen
         

         