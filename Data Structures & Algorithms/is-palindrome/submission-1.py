class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        right = len(s) - 1
        left = 0

        while left < right:
            while left < right and not self.isLetter(s[left]):
                left += 1
            while left < right and not self.isLetter(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True



    def isLetter(self, c:str) -> bool :
        return (ord("A") <= ord(c) <=ord("Z") or
        ord("a") <= ord(c) <=ord("z") or
        ord("0") <= ord(c) <=ord("9"))