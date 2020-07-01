# --------------------------------------------------------------------------
# Name:        Queue Reconstruction by Height
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Suppose you have a random list of people standing in a queue. Each 
    person is described by a pair of integers (h, k), where h is the height
    of the person and k is the number of people in front of this person who 
    have a height greater than or equal to h. Write an algorithm to 
    reconstruct the queue.

    Example
        Input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        Output: [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        
    Note: The number of people is less than 1,100.
    
    Hint #1:
        What can you say about the position of the shortest person?
        If the position of the shortest person is i, how many people 
        would be in front of the shortest person?
        
    Hint #2:
        Once you fix the position of the shortest person, what can you say 
        about the position of the second shortest person?
        
    Approach idea: H
        Have a list that sorted in desc order (taller person first). With 
        this, we can count the number of people that the new list that we
        current have and insert them to the k position by make use of k
          Given: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
          sort list = [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
          Insert 1st element, [7, 0]:
            newList = [[7, 0]]
                          ^ -> insert in index 0
          Insert 2nd element, [7, 1]:
            newList = [[7, 0], [7, 1]]
                                  ^ -> insert in index 1
          Insert 3rd element, [6, 1]:
            newList = [[7, 0], [6, 1], [7, 1]]
                                  ^ -> insert in index 1
          Insert 4th element, [5, 0]:
            newList = [[5, 0], [7, 0], [6, 1], [7, 1]]
                          ^ -> insert in index 0
          Insert 5th element, [5, 2]:
            newList = [[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]]
                                          ^ -> insert in index 2
          Insert 1st element, [4, 4]:
            newList = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
                                                          ^ -> insert in index 4
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort by h in DES then by k by ASC
        order = sorted(people, key=lambda i: (i[0], -i[1]), reverse=True)
        result = []
        
        for h, k in order:
            result.insert(k, (h,k))
        
        return result
            
         
                
        
        
        
 



        
'''other methods (from other submissions)
##################################################
def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output
'''
