class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ptr1 , ptr2 = len(a) -1 , len(b) - 1
        res = []
        carry = 0
        while ptr1 >= 0 or ptr2 >= 0 or carry:
            v1 = int(a[ptr1]) if ptr1 >= 0 else 0
            v2 = int(b[ptr2]) if ptr2 >= 0 else 0

            v = v1 + v2 + carry
            carry = v // 2
            res.append(str(v % 2))
            ptr1 -= 1
            ptr2 -= 1
        
        return "".join(reversed(res))