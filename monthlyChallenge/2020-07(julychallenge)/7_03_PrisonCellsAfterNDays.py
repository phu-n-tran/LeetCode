# --------------------------------------------------------------------------
# Name:        Prison Cells After N Days
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    There are 8 prison cells in a row, and each cell is either occupied or vacant.

    Each day, whether the cell is occupied or vacant changes according to the following rules:
      - If a cell has two adjacent neighbors that are both occupied or both vacant, 
        then the cell becomes occupied.
      - Otherwise, it becomes vacant.
      (Note that because the prison is a row, the first and the last cells in the 
      row can't have two adjacent neighbors.)

    We describe the current state of the prison in the following way: 
      cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

    Given the initial state of the prison, 
    return the state of the prison after N days (and N such changes described above.)



    Example 1:
      Input: cells = [0,1,0,1,1,0,0,1], N = 7
      Output: [0,0,1,1,0,0,0,0]
      Explanation: 
        The following table summarizes the state of the prison on each day:
          Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
          Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
          Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
          Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
          Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
          Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
          Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
          Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

    Example 2:
      Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
      Output: [0,0,1,1,1,1,1,0]


    Note:
      1. cells.length == 8
      2. cells[i] is in {0, 1}
      3. 1 <= N <= 10^9
"""

class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        # this help shorten and detect the cycle
        # loop at every 14th cycle
        N = (N - 1) % 14 + 1;
 
        temp = [0 for i in range(len(cells))]
        for i in range(N):
            for k in range(1, len(cells)-1):
                if cells[k-1] == cells[k+1]:
                    temp[k] = 1
                else:
                    temp[k] = 0
            print(temp)
            cells = temp[:]
        
        return cells
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def prisonAfterNDays(self, cells, N):
        # prev = cells[0]
        newN = ((N-1)%(14))
        
        for i in range(newN+1):
            prev = cells[0]
            for j in range(1,len(cells)-1):
                fornext = cells[j]
                cells[j] = 1 if (prev == cells[j+1]) else 0
                prev = fornext
            cells[0] = 0
            cells[len(cells)-1] = 0
        return cells
##################################################
def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        N -= max(N-1,0)//14*14
        for _ in range(N):
            cells = [0] + [cells[i-1]^cells[i+1]^1 for i in range(1,7)]+[0]
        return cells
##################################################
def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        if N > 14 :
            N %= 14
            
        if N %14 == 0:
            N = 14
     
        for i in range(N):
            cur = [0] * 8
            for j in range(1,7):
                if cells[j-1] == cells[j+1]:
                    cur[j] = 1
                else:
                    cur[j] = 0
            cells = cur
 
        return cur
'''
