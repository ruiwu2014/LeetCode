class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if target < A[0]:
            return 0

        if target > A[-1]:
            return len(A)

        for i in range (0,len(A)):
            if A[i] >= target:
                return i
