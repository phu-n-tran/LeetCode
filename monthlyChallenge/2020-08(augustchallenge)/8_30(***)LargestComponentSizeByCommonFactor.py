# --------------------------------------------------------------------------
# Name:        Largest Component Size by Common Factor
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a non-empty array of unique positive integers A, consider the following graph:

    There are A.length nodes, labelled A[0] to A[A.length - 1];
    There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
    Return the size of the largest connected component in the graph.

    Example 1:
      Input: [4,6,15,35]
      Output: 4

    Example 2:
      Input: [20,50,9,63]
      Output: 2

    Example 3:
      Input: [2,3,6,7,4,12,21,39]
      Output: 8

    Note:
      1. 1 <= A.length <= 20000
      2. 1 <= A[i] <= 100000
"""


class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = {}    # simple union find data structure
        def find(x):
            if x != d.setdefault(x,x):
                d[x] = find(d[x])
            return d[x]
        
        def union(x,y):
            d[find(x)]=find(y)

        for n in A:
            for i in range(2,int(n**0.5)+1): #just connect all the factors of the number  to the number
                if n%i: continue
                union(n,i)  
                union(n,n//i)

        counter = Counter(find(i) for i in A) 
        return max(counter.values())  # return the parent with maximum children
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
class UnionFind(object):
    def uf(self, n):  
        self.uf = [i for i in range(n)]
        self.size = [1] * n
        
    def find(self, x):  
        while x != self.uf[x]:
            self.uf[x] = self.uf[self.uf[x]]
            x = self.uf[x]
        return self.uf[x]

    def union(self, x, y):  
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.uf[x_root] = y_root
        self.size[y_root] += self.size[x_root]
        self.size[x_root] = 0


class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def primeFactors(n):  # Prime factor decomposition
            out = set()
            while n % 2 == 0: 
                out.add(2)
                n //= 2
            for i in range(3, int(math.sqrt(n))+1, 2): 
                while n % i== 0: 
                    out.add(i) 
                    n //= i 
            if n > 2: 
                out.add(n)
            return out
        
        uf = UnionFind()
        uf.uf(len(A))
        
        primeToIndex = {} 
        for i,a in enumerate(A):
            primes = primeFactors(a)
            for p in primes:
                if p in primeToIndex:
                    uf.union(i, primeToIndex[p])
                primeToIndex[p] = i
        return max(uf.size)
##################################################
def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if size[px] < size[py]:
                    px, py = py, px
                parents[py] = px
                size[px] += size[py]
        
        def prime_factors(num):
            factors = set()
            if num % 2 == 0:
                factors.add(2)
                while num % 2 == 0:
                    num /= 2
                    
            num_sqrt = int(math.sqrt(num)) + 1
            for i in range(3, num_sqrt, 2): 
                if num % i == 0:
                    factors.add(i)
                    while num % i == 0:
                        num /= i
                if num < i:
                    break
            if num > 2: 
                factors.add(num)
            return factors
        
        n = len(A)
        parents = range(n)
        size = [1] * n
        seen_factor = {}
        for i, num in enumerate(A):
            for factor in prime_factors(num):
                if factor in seen_factor:
                    union(i, seen_factor[factor])
                else:
                    seen_factor[factor] = i
        return max(size)
##################################################
def largestComponentSize(self, a):
        def parent(x):
            while root[x]!=x:
                root[x]=root[root[x]]
                x=root[x]
            return x
        
        def union(x,y):
            px=parent(x)
            py=parent(y)
            if px!=py:
                if size[px]>size[py]:
                    px,py=py,px
                size[py]+=size[px]
                root[px]=py
                
        def factorize(index,val):
            while val!=1:
                if smallestPrimeFactor[val] not in factorParent:
                    factorParent[smallestPrimeFactor[val]]=index
                union(index,factorParent[smallestPrimeFactor[val]])
                val/=smallestPrimeFactor[val]
                
        m=max(a)+1
        smallestPrimeFactor=range(m)
        for i in xrange(2,int(pow(m,0.5))+1):
            if smallestPrimeFactor[i]==i:
                for j in xrange(i*i,m,i):
                    if smallestPrimeFactor[j]==j:
                        smallestPrimeFactor[j]=i
                        
        n=len(a)
        size=[1]*n
        root=range(n)
        factorParent={}
        for i in xrange(n):
            factorize(i,a[i])
        return max(size)
'''
