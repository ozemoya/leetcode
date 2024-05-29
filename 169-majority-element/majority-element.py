class Solution:
    def majorityElement(self, nums: List[int]) -> int:  
        #Make a Hash
        freq = defaultdict(int)

        #make for loop evaluating 
        for num in nums:
            if num in freq.keys():
                freq[num]+= 1
            else:
                freq[num]=1
        
        #if you appear more than two times return val
            if freq[num] > (len(nums) / 2):
                return num