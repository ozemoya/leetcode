class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        reversed_words = word[::-1]
        reversed_string = ' '.join(reversed_words)
        return reversed_string