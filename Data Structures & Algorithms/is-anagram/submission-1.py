from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        mapi_s = {}
        mapi_t = {}

        for i in range(len(s)):
            mapi_s[s[i]] = 1 + mapi_s.get(s[i],0)
            mapi_t[t[i]] = 1 + mapi_t.get(t[i],0)

        for c in mapi_s:
            if mapi_s[c] != mapi_t.get(c,0):
                return False
        
        return True
        
