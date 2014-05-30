class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        size = 0
        for i in range(0,len(A)):
            if A[i] != elem:
                A[size]=A[i]
                size += 1
        return size
