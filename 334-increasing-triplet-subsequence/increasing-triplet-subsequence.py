class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
                
        return False

# Test the function with the given test case
solution = Solution()
print(solution.increasingTriplet([1, 2, 3, 4, 5]))  # Output should be True
print(solution.increasingTriplet([5, 4, 3, 2, 1]))  # Output should be False
print(solution.increasingTriplet([2, 1, 5, 0, 4, 6]))  # Output should be True