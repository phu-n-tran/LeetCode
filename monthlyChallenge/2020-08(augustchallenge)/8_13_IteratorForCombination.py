# --------------------------------------------------------------------------
# Name:        Iterator for Combination
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Design an Iterator class, which has:

    A constructor that takes a string characters of sorted distinct 
      lowercase English letters and a number combinationLength as arguments.
    A function next() that returns the next combination of length 
      combinationLength in lexicographical order.
    A function hasNext() that returns True if and only if there exists a next combination.


    Example:
    CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.
      iterator.next(); // returns "ab"
      iterator.hasNext(); // returns true
      iterator.next(); // returns "ac"
      iterator.hasNext(); // returns true
      iterator.next(); // returns "bc"
      iterator.hasNext(); // returns false


    Constraints:
      1. 1 <= combinationLength <= characters.length <= 15
      2. There will be at most 10^4 function calls per test.
      3. It's guaranteed that all calls of the function next are valid.
      
    Hints:
      1. Generate all combinations as a preprocessing.
      2. Use bit masking to generate all the combinations.
"""

class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        from itertools import combinations 
        
        self.combList = ["".join(combStr) for combStr in list(combinations(characters, combinationLength))]
        

    def next(self):
        """
        :rtype: str
        """
        return self.combList.pop(0)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.combList) > 0
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
        
        
        
    
        
            
        
 



        
'''other methods (from other submissions)
##################################################
class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.cur = characters[: combinationLength]
        self.is_poped = False
        self.characters = characters
        self.combinationLength = combinationLength

    def next(self):
        """
        :rtype: str
        """
        self.hasNext()
        self.is_poped = True
        return self.cur
            

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.is_poped:
            return True
        else:
            for i in range(self.combinationLength - 1, -1, -1):
                pos = self.characters.index(self.cur[i])
                if pos != len(self.characters) - self.combinationLength + i:
                    self.cur = self.cur[: i] + self.characters[pos + 1 : pos + 1 + self.combinationLength - i]
                    self.is_poped = False
                    return True
        return False
##################################################
def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.char = characters
        self.comb = combinationLength
        self.cur = 0
        
        self.comblist = [] 
        self.helper('', 0, self.comb, self.comblist,0)
 
        
    def helper(self, strin , ind, cap, res, cumu):
        if cumu == cap:
            res.append(strin)
            return 
        for i in range(ind, len(self.char)):
            self.helper( strin + self.char[i] , i+1, cap,res, cumu+1 )

    def next(self):
        """
        :rtype: str
        """
        self.cur += 1
        return self.comblist[self.cur - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur < len(self.comblist) 
##################################################
class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        res = []
        self.backtrack(res, '', characters, combinationLength, 0)
        
        self.queue = deque(res)

    def next(self):
        """
        :rtype: str
        """
        return self.queue.popleft()

    def hasNext(self):
        return len(self.queue) > 0
        
    def backtrack(self, res, combination, characters, combinationLength, start):
        if len(combination) == combinationLength:
            res.append(combination)
            
        for i in range(start, len(characters)):
            char = characters[i]
            self.backtrack(res, combination + char, characters, combinationLength, i + 1)
'''
