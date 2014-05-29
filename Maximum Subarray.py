class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        maxi = A
        maxi[0] = A[0]
        for i in range(1,len(A)):
            if A[i-1]< 0:
                maxi[i]=A[i]
            else:
                maxi[i]=A[i]+A[i-1]
        return max(maxi)

