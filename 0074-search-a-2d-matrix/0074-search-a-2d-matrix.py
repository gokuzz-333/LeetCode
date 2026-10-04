class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if len(matrix)==0:
            return False
        n=len(matrix)
        m=len(matrix[0])
        low=0
        high=m*n-1
        while low<=high:
            mid=low+(high-low)//2
            if matrix[mid//m][mid%m]==target:
                return True
            elif matrix[mid//m][mid%m]<target:
                low=mid+1
            else:
                high=mid-1
        return False
        