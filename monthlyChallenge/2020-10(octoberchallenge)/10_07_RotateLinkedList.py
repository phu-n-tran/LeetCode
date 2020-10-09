
# --------------------------------------------------------------------------
# Name:        Rotate List (Linked List)
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a linked list, rotate the list to the right by k places, where k is non-negative.

    Example 1:
      Input: 1->2->3->4->5->NULL, k = 2
      Output: 4->5->1->2->3->NULL
      Explanation:
        rotate 1 steps to the right: 5->1->2->3->4->NULL
        rotate 2 steps to the right: 4->5->1->2->3->NULL
    
    Example 2:
      Input: 0->1->2->NULL, k = 4
      Output: 2->0->1->NULL
      Explanation:
        rotate 1 steps to the right: 2->0->1->NULL
        rotate 2 steps to the right: 1->2->0->NULL
        rotate 3 steps to the right: 0->1->2->NULL
        rotate 4 steps to the right: 2->0->1->NULL
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # edge cases
        if head == None or head.next == None:
            return head
        
        # reduce the looping time
        count = 0;
        iterPtr = head 
        while iterPtr:
            count += 1
            iterPtr = iterPtr.next
        
        # update k
        k = k % count
        
        for i in range(k):
            # get to the last node
            tail = head 
            while tail.next:
                tail = tail.next
            
            # get to the second to last element (might be head if only 2 nodes)
            before_tail = head
            while before_tail.next != tail:
                before_tail = before_tail.next
            # print(before_tail.val, tail)
            
            before_tail.next = None
            tail.next = head
            head = tail
        return head
            
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """        
        if not head or not head.next:
            return head
        
        total = 0
        node = head
        while(node):
            total += 1
            node = node.next
        
        k = k%total
        if k == 0:
            return head
        
        fast = head
        for i in range(k):
            fast = fast.next
        
        slow = head
        
        while(fast.next):
            slow = slow.next
            fast = fast.next
        
        
        # 1-2-3-4-5-null
        # a   b c d
        
        a = head
        b = slow
        c = slow.next
        d = fast
        
        b.next = None
        d.next = a
        
        return c
##################################################
def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if(head==None):
            return None
        i = head
        n = 1
        while(i.next!=None):
            n+=1
            i = i.next
        j = k%n
        print("k: "+str(k)+" n: "+str(n)+" j: "+str(j))
        trv = head
        if(n-j-1>0):
            for x in range(n-j-1):
                trv = trv.next
        i.next = head
        head = trv.next
        trv.next = None
        return head
##################################################

##################################################
'''
