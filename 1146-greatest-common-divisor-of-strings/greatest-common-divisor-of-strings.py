from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenation in both orders is the same
        if str1 + str2 != str2 + str1:
            return ""
        
        # Compute the GCD of the lengths of str1 and str2
        gcd_length = gcd(len(str1), len(str2))
        
        # The GCD string is the prefix of str1 with length gcd_length
        return str1[:gcd_length]

# Example usage:
# solution = Solution()
# print(solution.gcdOfStrings("ABABAB", "ABAB"))  # Output should be "AB"