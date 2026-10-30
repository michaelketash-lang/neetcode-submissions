class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        substring = []

        def backtrack(openP , closeP):
            if openP == closeP and openP == n:
                sub = "".join(substring)
                res.append(sub)
                return
            
            if openP < n:
                substring.append("(")
                backtrack(openP + 1 , closeP)
                substring.pop()
            
            if closeP < openP:
                substring.append(")")
                backtrack(openP , closeP + 1)
                substring.pop()
        
        backtrack(0 , 0)
        return res