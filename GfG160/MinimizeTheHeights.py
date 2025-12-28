"""
Given an array arr[] denoting heights of n towers and a positive integer k.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by k
Decrease the height of the tower by k
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

Note: It is compulsory to increase or decrease the height by k for each tower. After the operation, the resultant array should not contain any negative integers.
"""
class Solution:
    def getMinDiff(self, arr, k):
        # code here
        n = len(arr)
        arr.sort()
        dif = arr[n-1] - arr[0]
        
        for idx in range(1,n):
            if arr[idx] < k:
                continue
            
            min_val = min(arr[0] + k, arr[idx] - k)
            max_val = max(arr[idx - 1] + k, arr[n-1] - k)
            
            dif = min(dif, max_val - min_val)
        
        return dif
        