class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        #Two Pointer Method including first and second
        first = 0 
        second = int(c**0.5)
        while first <= second:
            #first and second squared equals current sum 
            current_sum = first**2 + second**2
            if current_sum == c:
                return True
            elif current_sum < c: 
                first += 1
            else:
                second -=1
        return False