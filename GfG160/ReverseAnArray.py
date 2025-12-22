"""
You are given an array of integers arr[]. You have to reverse the given array.

Note: Modify the array in place.
"""
class Solution:
    def reverseArray(self, arr):
        # code here
        n = len(arr)
        temp = [0] * n
        
        j = n-1
        
        for i in arr:
            temp[j]=i
            j = j-1
        
        for i in range(len(arr)):
            arr[i]=temp[i]
        