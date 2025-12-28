"""
You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].

Note : A subarray is a continuous part of an array.
"""
class Solution:
    def maxSubarraySum(self, arr):
        maxSum = arr[0]
        maxEnd = arr[0]
        
        for idx in range(1, len(arr)):
            
            maxEnd = max(maxEnd + arr[idx], arr[idx])
            maxSum = max(maxEnd, maxSum)
        
        return maxSum
        