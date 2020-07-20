# --------------------------------------------------------------------------
# Name:        Remove Linked List Elements
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Remove all elements from a linked list of integers that have value val.

    Example:
      Input:  1->2->6->3->4->5->6, val = 6
      Output: 1->2->3->4->5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head is not None and head.val == val:
            head = head.next
        
        if head is None:
            return None
        curPtr = head
        prevPtr = ListNode(next=head)
            
            
        while curPtr:
            # print(prevPtr.val, curPtr.val)
            if curPtr.val == val:
                prevPtr.next = curPtr.next
                
                curPtr = curPtr.next
                # or
                # curPtr.next = None
                # curPtr = prevPtr.next
            else:
                prevPtr = prevPtr.next
                curPtr = curPtr.next
            
        
        return head
            
        
                
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = TreeNode()
        dummy.next = head
        prev, node = dummy, head
        
        while node:
            
            if node.val == val:
                prev.next = node.next
            else:
                prev = node
            
            node = node.next
        
        return dummy.next
##################################################
def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None: 
            return None
            
        prev = None
        cur = head
        
        while cur is not None:
            if cur.val == val:
                if prev is not None:
                    prev.next = cur.next
                    cur = cur.next
                else:
                    head = head.next
                    prev = None
                    cur = head
            else:
                prev = prev.next if prev is not None else head
                cur = cur.next
        return head
##################################################
'''
