class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        diagon_sum = 0
        i = 0
        
        for i in range(len(mat)):
            diagon_sum += mat[i][i]
            
        for i in range(len(mat)):  
            if i == len(mat) -1 -i:
                    continue  
            diagon_sum += mat[i][len(mat) -1 - i]
            
        return diagon_sum
