class Solution:
    def countBits(self, n: int) -> List[int]:
        count = []
        for i in range(n + 1):
            count.append(self.countBit(i))
        return count

    def countBit(self , n):
        count = 0

        while n != 0:
            count += (n & 1)
            n >>= 1

        
        return count