
# --------------------------------------------------------------------------
# Name:        Odd Even Linked List
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a singly linked list, group all odd nodes together followed by the
    even nodes. Please note here we are talking about the node number and
    not the value in the nodes.

    You should try to do it in place. The program should run in O(1) space 
    complexity and O(nodes) time complexity.
    
    Example 1:
        Input: 1->2->3->4->5->NULL
        Output: 1->3->5->2->4->NULL
    
    Example 2:
        Input: 2->1->3->5->6->4->7->NULL
        Output: 2->3->6->7->1->5->4->NULL
    
    Note: 
        1) The relative order inside both the even and odd groups should 
           remain as it was in the input.
        2) The first node is considered odd, the second node even and so on ...
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        # act as iterate pointer for odd
        oddHead = head
        # point to the head of the first even position 2 and not moving
        evenHead = head.next
        # act as iterate pointer for even
        iterEven = evenHead     
        # iterate pointer
        iterHead = evenHead.next
        
        while iterHead is not None:
            # iterHead is in odd position, update odd
            oddHead.next = iterHead
            oddHead = iterHead
            
            # move iterate pointer to even position
            iterHead = iterHead.next
            if iterHead is None:
                break
            
            # iterHead is in even position, update even
            iterEven.next = iterHead
            iterEven = iterHead
            
            # move iterate pointer to odd position
            iterHead = iterHead.next
        
        # take the end of odd and attach it to the begin of even
        oddHead.next = evenHead
        # update the end of even to prevent cycle in the linked list
        iterEven.next = None
            
        return head







        
"""other faster methods (from other submissions)
##################################################
def oddEvenList(self, head):
      """
      :type head: ListNode
      :rtype: ListNode
      """
      if not head: return head
      odd, even, dummy = head, head.next, head.next

      while even and even.next:
          odd.next, odd = odd.next.next, odd.next
          odd = odd.next
          even.next = even.next.next
          even = even.next
      odd.next = dummy
      return head
"""
