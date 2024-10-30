from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1  # If there's only one person, they are the judge by default.

        trust_count = [0] * (n + 1)
        outgoing_trust = [0] * (n + 1)

        for a, b in trust:
            outgoing_trust[a] += 1  # Person 'a' trusts someone.
            trust_count[b] += 1     # Person 'b' is trusted by 'a'.

        for i in range(1, n + 1):
            if trust_count[i] == n - 1 and outgoing_trust[i] == 0:
                return i  # Found the judge.

        return -1  # No judge found.