"""
Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.
"""

#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        temp = [0] * len(arr)
        
        for i in range(len(arr)):
            j = i - d
            while j < 0:
                j = j + len(arr)
            temp[j] = arr[i]
        
        for i in range(len(arr)):
            arr[i] = temp[i]