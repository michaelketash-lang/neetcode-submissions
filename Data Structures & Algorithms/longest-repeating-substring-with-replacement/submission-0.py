class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #initialize a hashmap
        count = {} #key-letter:val -freq
        #left
        l = 0
        res = 0
        for r in range(len(s)):
            # update the freq of a letter
            count[s[r]] = 1 + count.get(s[r],0)
            #it's true when size of window[i,j] - most freq letteris bigger then k
            while (r - l +1) - max(count.values()) > k:
                count[s[l]] -= 1 #decrement the freq
                l += 1 #make the window smaller
            res = max(r - l +1,res) #max between window size and res
        return res