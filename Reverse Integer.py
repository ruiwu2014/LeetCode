class Solution:
    # @return an integer
    def reverse(self, x):
        sign=True
        res=0
        if x<0:
            x=-x
            sign=False
        while x!=0:
           res = res*10+x%10
           x=x/10
        if sign:
            return res
        else:
            return -res