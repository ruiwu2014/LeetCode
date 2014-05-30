class Solutions:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        red, white, blue = 0,0,0 #red: 0, white: 1, blue: 2
        index = 0
        for i in A:
            if i == 0:
                red += 1
                A[index] = 0
                index+=1
            elif i == 1:
                white += 1
            else:
                blue +=1
        for i in range(index+1,index+white):
            A[i] = 1         
        for i in range(index+white,len(A)):
            A[i] = 2
                
 
              
        