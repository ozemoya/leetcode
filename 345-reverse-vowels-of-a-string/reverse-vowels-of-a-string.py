class Solution:
    def reverseVowels(self, s: str) -> str:
        output = []
        vowels = [char for char in s if char in "aeiouAEIOU"]
        vowels = vowels[::-1]
        for char in s: 
            if char in "aeiouAEIOU":
                output.append(vowels.pop(0))
            else:
                output.append(char)
        return "".join(output)
