from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: Initialize the left_products and right_products arrays
        left_products = [1] * n
        right_products = [1] * n
        result = [1] * n
        
        # Step 2: Compute left_products
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]
        
        # Step 3: Compute right_products and the result array
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]
        
        for i in range(n):
            result[i] = left_products[i] * right_products[i]
        
        return result

# Example usage:
solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))  # Output: [0, 0, 9, 0, 0]