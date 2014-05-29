class Solution:
    # @return an integer
    def numTrees(self, n):
        arrs = [0] *(n+1)
        if n<=1:
            return n
        arrs[0] = 1
        arrs[1] = 1
        arrs[2] = 2
        return self.numTreesR(n,arrs)



    def numTreesR(self, n, a):
        i = 3
        while i <= n:
            for j in range(0,i):
                a[i] += a[j]*a[i-j-1]
            i += 1
        return a[n]



