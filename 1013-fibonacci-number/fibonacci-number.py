class Solution:
    def fib(self, n: int) -> int:
        GOLDEN_RATIO = 1.618034
        return int((math.pow(GOLDEN_RATIO, n) - math.pow(1 - GOLDEN_RATIO, n)) / math.sqrt(5))