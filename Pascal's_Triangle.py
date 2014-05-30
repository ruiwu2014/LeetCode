class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        res = []
        if numRows == 0:
            return res
        if numRows==1:
            res.append([1])
            return res
        if numRows == 2:
            res.append([1])
            res.append([1,1])
            return res
        res = self.generate(numRows-1)
        lastRow = res[-1]
        current = [1]
        for i in range(1,len(lastRow)):
            current.append(lastRow[i-1]+lastRow[i])
        current.append(1)
        res.append(current)
        return res