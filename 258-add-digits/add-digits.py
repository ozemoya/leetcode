class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Keep looping as long as the number has more than one digit
        while num >= 10:
            current_sum = 0
            # Convert the number to a string to iterate through its digits
            for digit_char in str(num):
                # Convert the digit character back to an integer and add it
                current_sum += int(digit_char)
            
            # Set 'num' to the new sum for the next loop
            num = current_sum
            
        # Once the loop finishes, 'num' will be a single digit
        return num

# --- How it works: ---
# sol = Solution()
# sol.addDigits(38)
#
# 1. num = 38.  (38 >= 10, so loop starts)
# 2. current_sum = 0
# 3. Loop through "38":
#    - current_sum += int("3")  (current_sum is 3)
#    - current_sum += int("8")  (current_sum is 11)
# 4. Set num = 11
#
# 5. num = 11.  (11 >= 10, so loop continues)
# 6. current_sum = 0
# 7. Loop through "11":
#    - current_sum += int("1")  (current_sum is 1)
#    - current_sum += int("1")  (current_sum is 2)
# 8. Set num = 2
#
# 9. num = 2.   (2 < 10, loop stops)
# 10. Return 2