class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers aur last digit 0 (except 0 itself) palindrome nahi ho sakte
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        rev = 0
        
        # Sirf half number reverse karo
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        
        # Even digits case: x == rev
        # Odd digits case: x == rev // 10
        return x == rev or x == rev // 10