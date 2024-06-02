class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #output 
        output = []
        #set max candy
        max_candy = max(candies)
        #make for loop 
        for i in range(len(candies)):
            kid = candies[i]
            if kid + extraCandies >= max_candy:
                output.append(True)
            else:
                output.append(False)
        return output
