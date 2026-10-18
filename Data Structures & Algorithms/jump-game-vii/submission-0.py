class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0

        while q:
            indx = q.popleft()

            start = max(indx + minJump , farthest + 1)

            for j in range(start , min(indx + maxJump + 1 , len(s))):
                if s[j] == "0":
                    q.append(j)
                    if j == len(s) - 1:
                        return True
            
            farthest = indx + maxJump

        return False