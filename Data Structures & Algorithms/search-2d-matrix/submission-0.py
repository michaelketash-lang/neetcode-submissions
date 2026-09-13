class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # keep the bounds of the matrix
        ROWS , COLS = len(matrix) , len(matrix[0])
        # look as a long 1d array
        l , r = 0 , ROWS*COLS -1
        
        # binary search
        while l <= r:
            mid = (l + r) // 2
            # row : mid // COLS
            # col : mid % COLS
            val = matrix[mid // COLS][mid % COLS]
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return True
        return False