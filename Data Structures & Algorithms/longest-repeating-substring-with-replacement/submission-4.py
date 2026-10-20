class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Part A initialization
        left = longest = maximum = 0
        hashMap = {}

        # Part B to be a for loop that will increment the right pointer
        for r in range(len(s)):
            hashMap[s[r]] = 1 + hashMap.get(s[r] , 0)
            maximum = max(maximum , hashMap[s[r]])
        # Part C to check if we broke the constraint 
            while (r - left + 1) - maximum > k:
                hashMap[s[left]] -= 1
                left += 1
        
        # Pard D update the longest substring
            longest = max(longest , r - left + 1)
        
        return longest