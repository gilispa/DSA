"""
Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

Note: It is guaranteed that the answer fits in a 32-bit integer.
"""
class Solution:
	def maxProduct(self,arr):
		# code here
		maxProduct = arr[0]
		minProduct = arr[0]
		globalMax = arr[0]
		
		for i in range(1, len(arr)):
		    if arr[i] < 0:
		        maxProduct, minProduct = minProduct, maxProduct
	        
	        maxProduct = max(arr[i], maxProduct * arr[i])
	        minProduct = min(arr[i], minProduct * arr[i])
	        
	        globalMax = max(globalMax, maxProduct)
	        
        return globalMax
