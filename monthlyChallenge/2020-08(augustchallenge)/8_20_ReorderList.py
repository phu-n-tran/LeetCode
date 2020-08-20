# --------------------------------------------------------------------------
# Name:        Reorder List
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a singly linked list L: L0→L1→…→Ln-1→Ln,
    reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

    You may not modify the values in the list's nodes, only nodes itself may be changed.

    Example 1:
      Given 1->2->3->4, reorder it to 1->4->2->3.
      
    Example 2:
      Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return []
        stack = []
        ite = head
        
        while ite:
            stack.append(ite)
            ite = ite.next
        
        tail = stack.pop()
        ite = head
        
        while tail != ite:
            dummy = ite.next
            if dummy == tail:
                break
                
            ite.next = tail
            tail.next = dummy
            ite = dummy
            tail = stack.pop()
        
        tail.next = None
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        secondHead = slow.next
        slow.next = None
        if secondHead:
            prev = None
            curr = secondHead
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            
            curr1 = head
            curr2 = prev
            while curr1 and curr2:
                newNext = curr1.next
                curr1.next = curr2
                curr1 = curr2
                curr2 = newNext
##################################################
def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #Find midpoint
        if not head: return None
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #Reverse the second part        
        prev,curr = None,slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #Combine two list
        first,second = head, prev
        while second and second.next:
            first.next,first = second,first.next
            second.next,second = first,second.next
##################################################
def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # find middle with slow and fast pointers
        # reverse second half
        # merge two lists
        if not head:
            return
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next # Start of new list
        slow.next = None

        prev = None
        p = mid
        while p != None:
            nextnext = p.next
            p.next = prev
            prev = p
            p = nextnext
        
        #prev is now start of second half
        p1 = head
        p2 = prev
        while p1 and p2:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
'''
