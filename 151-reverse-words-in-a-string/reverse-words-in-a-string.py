class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Test Case:
        Input: Input: s = "the sky is blue"
        Output: "blue is sky the"
        """
        s_split = s.split()
        reversed_s = reversed(s_split)
        return " ".join(reversed_s)