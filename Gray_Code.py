class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n ==0:
            return [0]
        if n == 1:
            res = [0,1]
            return res
        if n> 1:
            arr = self.grayCode(n-1)
            rev = arr[::-1]
            for i in range(0,len(rev)):
                rev[i] += (1<<(n-1))
            return arr+rev