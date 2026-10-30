class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        q = deque([n])
        visit = set()
        visit.add(n)
        level = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for square in squares:
                    remainder = node - square
                    if remainder == 0:
                        return level

                    if remainder < 0:
                        break

                    if remainder not in visit:
                        visit.add(remainder)
                        q.append(remainder)

            level += 1 
        return -1
