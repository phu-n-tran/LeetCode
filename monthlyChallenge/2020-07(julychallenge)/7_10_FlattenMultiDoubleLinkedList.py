# --------------------------------------------------------------------------
# Name:        Flatten a Multilevel Doubly Linked List
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You are given a doubly linked list which in addition to the next and 
    previous pointers, it could have a child pointer, which may or may not
    point to a separate doubly linked list. These child lists may have one
    or more children of their own, and so on, to produce a multilevel data 
    structure, as shown in the example below.

    Flatten the list so that all the nodes appear in a single-level, doubly 
    linked list. You are given the head of the first level of the list.

    Example 1:
      Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
      Output: [1,2,3,7,8,11,12,9,10,4,5,6]
    Explanation:
      **SEE IMAGE 7_10_example1_pic.PNG

    Example 2:
      Input: head = [1,2,null,3]
      Output: [1,3,2]
      Explanation:
        The input multilevel linked list is as follows:

          1---2---NULL
          |
          3---NULL
          
    Example 3:
      Input: head = []
      Output: []
      
      
    How multilevel linked list is represented in test case:
      We use the multilevel linked list from Example 1 above:
         1---2---3---4---5---6--NULL
                 |
                 7---8---9---10--NULL
                     |
                     11--12--NULL
    The serialization of each level is as follows:
      [1,2,3,4,5,6,null]
      [7,8,9,10,null]
      [11,12,null]
     
    To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:
      [1,2,3,4,5,6,null]
      [null,null,7,8,9,10,null]
      [null,11,12,null]
    
    Merging the serialization of each level and removing trailing nulls we obtain:
      [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]

    Constraints:
      1. Number of Nodes will not exceed 1000.
      2. 1 <= Node.val <= 10^5
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def helper(head):
            """
            use recursion when meet nodes with child and explore it first
            """
            curPtr = None
            flag = True
            
            while head and flag:
                if head.child is not None:
                    # save the node that the last child in the list that will connect to
                    curPtr = head.next
                    
                    helper(head.child)
                    
                    # after finish with the child, update the pointers of the parent
                    head.next = head.child
                    head.child.prev = head
                    head.child = None
                    
                if head.next:
                    head = head.next
                else:
                    flag = False
                    
            if curPtr is not None:
                curPtr.prev = head
            
            # curPtr can be None or a node element
            head.next = curPtr
        
        if head is None or head.next is None and head.child is None:
            return head
        
        temp = head
        helper(temp)
 
        return head

       
                
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        stack=[]
        if head is None:return head
        dummy=Node(0,None,head,None)
        dummy.next=head
        prev=dummy
        curr=head
        stack.append(curr)
        
        while(len(stack)!=0):
            
            curr=stack.pop()
            curr.prev=prev
            prev.next=curr
            prev=prev.next
            
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                
                curr.child=None
            
        dummy.next.prev=None
        return dummy.next
        
        # if not head:return None
        # dummy=Node(0,None,head,None)
        # prev=dummy
        # curr=head
#         self.dfs(prev,curr)
#         dummy.next.prev=None
#         return dummy.next   
#     def dfs(self,prev,curr):
#         if curr is None:
#             return prev
#         curr.prev=prev
#         prev.next=curr
#         tempright=curr.next
#         tail=self.dfs(curr,curr.child)
#         curr.child=None
#         return self.dfs(tail,tempright)
        
        
        #newNode.prev=node.prev
        # print(newNode)
        # return newNode
##################################################
 def flatten(self, head):
        if not head:
            return 
        dummy=Node(0,None,head,None)
        prev=dummy
        stack=[head]
        while len(stack)!=0:
            root=stack.pop()
            root.prev=prev
            prev.next=root
            if root.next:
                stack.append(root.next)
                root.next=None
            if root.child:
                stack.append(root.child)
                root.child=None
            prev=root
        dummy.next.prev=None   
        return dummy.next
##################################################
def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        stack = []
        dummy = Node(0,None,None,None)
        cur = dummy
        stack.append(head)
        while len(stack)>0:
            new = stack.pop()
            if new.next:
                stack.append(new.next)
            if new.child:
                stack.append(new.child)
            new.child = None
            cur.next = new
            new.prev = cur
            cur = cur.next
            
        # cur.next = None
        new_head = dummy.next
        new_head.prev = None
        return new_head
'''
