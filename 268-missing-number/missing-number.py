class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)  # Convert the input list to a set
        for i in range(len(nums)+1):  # Iterate over the range of the input list length + 1
            if i not in nums_set:  # Check if the current number is missing in the set
                return i  # Return the first missing number found

