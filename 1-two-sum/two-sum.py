class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        hashmap: 0:2, 0:3, 0:11, 0:15
        """
        hashmap = {}
        #enumerate for loop
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in hashmap:
                return [hashmap[compliment], i]
            hashmap[num] = i
                



            
