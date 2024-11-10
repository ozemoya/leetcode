class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left(nums, target):
            left = 0 
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else: 
                    left = mid + 1
            return left


        def find_right(nums, target):
            left = 0 
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else: 
                    right = mid - 1
            return right

        start, end = find_left(nums,target), find_right(nums,target)

        if start <= end and start < len(nums) and nums[start] == target:
            return [start, end]
        return [-1, -1]