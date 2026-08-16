class Solution:
    def countBits(self, n: int) -> List[int]:
        #dynamic prog
        my_output=[0]
        for i in range(1,n+1):
            my_output.append(my_output[i//2]+i%2)
        return my_output

        