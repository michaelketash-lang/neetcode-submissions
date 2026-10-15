class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX = 0x7FFFFFFF

        while b != 0:
            carry = ((a & b) << 1 )& MASK
            a = (a ^ b) & MASK
            b = carry
        
        if a > MAX:
            a = a - (1 << 32)
        return a

