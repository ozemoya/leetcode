class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #TC: [1,2,3,4,5]
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False