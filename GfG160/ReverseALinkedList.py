'''
You are given the head of a singly linked list. You have to reverse the linked list and return the head of the reversed list.
'''
"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        # Code here
        stack = []
        current = head
        
        while current:
            stack.append(current)
            current = current.next
            
        new_head = stack.pop()
        current = new_head
        
        while stack:
            node = stack.pop()
            current.next = node
            current = node
            
        current.next = None
            
        return new_head