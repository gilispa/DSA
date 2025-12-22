"""
Given an array arr[] consisting of n integers, the task is to find all the array elements which occurs more than floor(n/3) times.

Note: The returned array of majority elements should be sorted.
"""
class Solution:
    def findMajority(self, arr):
        # code here
        n = len(arr)
        r = []
        frec = {}
        
        for ele in arr:
            frec[ele] = frec.get(ele, 0) + 1
            
        for ele, count in frec.items():
            if count > n//3:
                r.append(ele)
                
        if len(r) == 2 and r[0]>r[1]:
            r[0],r[1] = r[1],r[0]
                
        return r