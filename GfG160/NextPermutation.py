"""
Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

Note:  A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.
"""

class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        pivot = -1
        for ele in range(len(arr) - 2, -1, -1):
            if arr[ele] < arr[ele + 1]:
                pivot = ele
                break
        
        if pivot == -1:
            arr.reverse()
            return arr
        
        for ele in range(len(arr) - 1, -1, -1):
            if pivot == ele:
                break
            if arr[pivot] < arr[ele]:
                arr[pivot], arr[ele] = arr[ele], arr[pivot]
                break
        
        left, right = pivot + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right] , arr[left]
            left = left + 1
            right = right - 1 
            
        return arr