class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #setting up boundries
        if not matrix:
            return []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []
        
        while top <= bottom and left <= right:
            # Traverse Right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # Traverse Down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # Traverse Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            # Traverse Up
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result






