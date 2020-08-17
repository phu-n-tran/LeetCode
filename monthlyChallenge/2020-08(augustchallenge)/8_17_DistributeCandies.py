# --------------------------------------------------------------------------
# Name:        Distribute Candies to People
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    We distribute some number of candies, to a row of n = num_people people
    in the following way:

    We then give 1 candy to the first person, 2 candies to the second person,
    and so on until we give n candies to the last person.

    Then, we go back to the start of the row, giving n + 1 candies to the 
    first person, n + 2 candies to the second person, and so on until we 
    give 2 * n candies to the last person.

    This process repeats (with us giving one more candy each time, and moving
    to the start of the row after we reach the end) until we run out of candies.
    The last person will receive all of our remaining candies 
    (not necessarily one more than the previous gift).

    Return an array (of length num_people and sum candies) that represents 
    the final distribution of candies.

    Example 1:
      Input: candies = 7, num_people = 4
      Output: [1,2,3,1]
      Explanation:
        On the first turn, ans[0] += 1, and the array is [1,0,0,0].
        On the second turn, ans[1] += 2, and the array is [1,2,0,0].
        On the third turn, ans[2] += 3, and the array is [1,2,3,0].
        On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].

    Example 2:
      Input: candies = 10, num_people = 3
      Output: [5,2,3]
      Explanation: 
        On the first turn, ans[0] += 1, and the array is [1,0,0].
        On the second turn, ans[1] += 2, and the array is [1,2,0].
        On the third turn, ans[2] += 3, and the array is [1,2,3].
        On the fourth turn, ans[0] += 4, and the final array is [5,2,3].

    Constraints:
      1. 1 <= candies <= 10^9
      2. 1 <= num_people <= 1000
      
    Hint:
      1. Give candy to everyone each "turn" first [until you can't], 
         then give candy to one person per turn.
"""

class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        result = [0]*num_people
        give = 1
        index = 0
        
        while candies > 0:
            # if candies still more than give
            if candies >= give:
                result[index] += give
                candies -= give
                give += 1
                index += 1
                if index == num_people:
                    index = 0
            else:
                result[index] += candies
                candies = 0
        return result
        
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0 for i in range(num_people)]

        candy_to_give = 1
        i = 0
        while(candies>0):
            if candies < candy_to_give:
                res[i%num_people] += candies
                return res
            res[i%num_people] += candy_to_give
            i += 1
            candies -= candy_to_give
            candy_to_give += 1
        return res
##################################################
def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        ppl = [0]*num_people
        n = 0
        while candies >= 0:
            for i in range(len(ppl)):
                if candies - (n + i + 1) > 0:
                    ppl[i] += n + i + 1
                    candies -= n + i + 1
                else:
                    ppl[i] += candies
                    candies -= n + i + 1
                    break
            n += len(ppl)
        return ppl
##################################################
def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        
        distribution = []
        n = candies

        for person in range(1,num_people+1):
            if n > person:
                distribution.append(person)
                n -= person
            else:
                distribution.append(n)
                n = 0

        incrementer = len(distribution) + 1

        while n > 0:
            i = 0
            for x in distribution:
                if n > 0: 
                    if n >= incrementer:
                        distribution[i] += incrementer
                    else:
                        distribution[i] += n

                    n -= incrementer
                    i += 1
                    incrementer += 1

        return distribution
'''
