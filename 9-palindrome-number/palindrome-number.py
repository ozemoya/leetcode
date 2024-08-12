class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        #Convert x to string and then use two Pointer method first and last
        str_x = str(x)
        first = 0
        last = len(str_x)-1
        while first <= last:
            if str_x[first] != str_x[last]:
                return False
            first +=1
            last -=1
        return True
    