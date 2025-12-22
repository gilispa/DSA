"""
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.
"""

class Solution:
    def getSecondLargest(self, arr):
        l = -1
        secl = -1
        # Code Here
        for num in arr:
            if num>l:
                secl=l
                l=num
            elif num>secl and num!=l:
                secl=num
        return secl