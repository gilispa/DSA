"""
Given an array arr[] of integers and another integer target. Determine if there exist two distinct indices such that the sum of their elements is equal to the target.
"""

class Solution:
	def twoSum(self, arr, target):
		# code here
		hash = set()
		
		for num in arr:
		    complement = target - num
		    if complement in hash:
		        return True
	        hash.add(num)
        
        return False