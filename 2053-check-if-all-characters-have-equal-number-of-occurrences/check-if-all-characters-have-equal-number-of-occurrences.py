class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s: 
            counts[c] += 1
        frequency = counts.values()
        return(len(set(frequency))) == 1