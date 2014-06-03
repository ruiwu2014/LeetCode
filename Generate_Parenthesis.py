class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        return self.generateParenthesisR(n,n)
        
    def generateParenthesisR(self, l, r):
        res = []
        if l == 0:
            str = ')'*r
            res.append(str)
            return res
        
        if l == r:
            res = self.generateParenthesisR(l-1,r)
            for i in range(0,len(res)):
                res[i] = '(' + res[i]
            return res
        if l < r:
            addL = self.generateParenthesisR(l-1,r)
            addR = self.generateParenthesisR(l,r-1)
            for i in range(0,len(addL)):
                addL[i] = '(' + addL[i]
            for i in range(0,len(addR)):
                addR[i] = ')' + addR[i]
            res =addL + addR
            return res
        