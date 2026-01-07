"""
You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1. The array can have negative integers too.
"""
class Solution:
    def missingNumber(self, arr):
        # code here
        numbers = set()
        
        for num in arr:
            numbers.add(num)
        
        i = 1
        while i in numbers:
            i += 1
            
        return i
            