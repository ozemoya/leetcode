class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                # Check if the previous and next plots are empty or out of bounds
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)
                next_empty = (i == length - 1 or flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    # Plant a flower here
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return n <= 0