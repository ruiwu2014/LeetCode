class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n <= 2:
            return n
        A = [0]*n
        A[0] = 1
        A[1] = 2
        A =self.climbStairsR(A,n)
        return A[-1]


    def climbStairsR(self,A,n):
        if n<=2:
            return A[n]
        if n == 3:
            A[2] = A[0]+A[1]
            return A
        if A[n-2] and A[n-3]:
            A[n-1] = A[n-2]+A[n-3]
        else:
            A = self.climbStairsR(A,n-1)
            A[n-1] = A[n-2]+A[n-3]

        return A
