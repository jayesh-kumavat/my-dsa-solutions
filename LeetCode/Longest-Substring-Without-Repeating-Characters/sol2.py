# DSA Tracker | Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# DSA Tracker | Language: Python3
# DSA Tracker | Difficulty: Medium
# DSA Tracker | Topics: Hash Table, String, Sliding Window
# DSA Tracker | Runtime: 159 ms — beats 78.48% of submissions
# DSA Tracker | Memory: 19.8 MB — beats 76.45% of submissions

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charMap = {}
        left = 0
        
        for right in range(n):
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right
        
        return maxLength
