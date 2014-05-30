class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)<=1:
            return len(A)
        sz = 0
        for i in range(1,len(A)):
            if A[i] != A[sz]:
                A[sz+1]=A[i]
                sz +=1
        return sz+1