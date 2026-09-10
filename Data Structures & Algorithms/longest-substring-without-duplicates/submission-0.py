class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set() # Set to track characters in the current window
        l = 0 # Left pointer of the window
        result = 0 # Variable to store the max length found
        
        for r in range(len(s)): # Iterate with right pointer 'r'
            # Contract the window from the left until the duplicate is removed
            while s[r] in char_set:
                char_set.remove(s[l]) # Remove the leftmost character
                l += 1 # Shrink window from the left
            
            char_set.add(s[r]) # Add the new character to the window
            result = max(result, r - l + 1) # Update max length if needed
            
        return result