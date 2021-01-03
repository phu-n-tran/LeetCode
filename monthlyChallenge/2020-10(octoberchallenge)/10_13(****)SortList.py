# --------------------------------------------------------------------------
# Name:        Sort List
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given the head of a linked list, return the list after sorting it in ascending order.

    Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?


    Example 1:
      Input: head = [4,2,1,3]
      Output: [1,2,3,4]
    
    Example 2:
      Input: head = [-1,5,3,4,0]
      Output: [-1,0,3,4,5]
    
    Example 3:
      Input: head = []
      Output: []

    Constraints:
      1) The number of nodes in the list is in the range [0, 5 * 104].
      2) -105 <= Node.val <= 105
      
    Note: solution is online (bottom-up approach)
    https://leetcode.com/problems/sort-list/solution/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        def getSize(head):
            # Simply count the length of linked list
            counter = 0
            while head:
                counter +=1
                head = head.next
            return counter
        
        def split(head, size):
            # given the head & size, return the the start node of next chunk
            for i in range(size-1): 
                if not head: 
                    break 
                head = head.next

            if not head: return None
            next_start, head.next = head.next, None  #disconnect
            
            return next_start
        
        def merge(l1, l2, dummy_start):
            # Given dummy_start, merge two lists, and return the tail of merged list
            curr = dummy_start
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next, l1 = l1, l1.next
                else:
                    curr.next, l2 = l2, l2.next
                curr = curr.next
            
            curr.next = l1 if l1 else l2
            while curr.next: curr = curr.next  # Find tail
            # the returned tail should be the "dummy_start" node of next chunk
            return curr  

        total_length = getSize(head)
        dummy = ListNode(0)
        dummy.next = head
        start, dummy_start, size = None, None, 1
        
        while size < total_length:
            dummy_start = dummy
            start = dummy.next 
            while start:
                left = start
                right = split(left, size) # start from left, cut with size=size
                start = split(right, size) # start from right, cut with size=size
                dummy_start = merge(left, right, dummy_start)  # returned tail = next dummy_start 
            size *= 2
        return dummy.next
        
        
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # store the values, sort
        # fill in the values
        lst = []
        
        cur_node = head
        while cur_node!=None:
            lst.append(cur_node.val)
            cur_node= cur_node.next
        
        lst = sorted(lst)
        cur_node = head
        i = 0
        while cur_node!=None:
            cur_node.val = lst[i]
            i+=1
            cur_node=cur_node.next
        return head
##################################################
##################################################
##################################################
'''
