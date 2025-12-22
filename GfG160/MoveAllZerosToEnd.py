"""
You are given an array arr[] of non-negative integers. You have to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.
"""
class Solution:
	def pushZerosToEnd(self, arr):
	    n = len(arr)
	    temp = [0] * n 
	    j = 0
	    
	    for i in arr:
	        if i != 0:
	            temp[j] = i
	            j = j + 1
	   
        for i in range(len(arr)):
            arr[i]=temp[i]