def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(A)-2):
            while i<len(A)-2 and A[i+2] -A[i+1] == A[i+1]-A[i]:
                count +=1
                i += 1 
        return count
