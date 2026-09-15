# DSA Tracker | Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# DSA Tracker | Language: Python3
# DSA Tracker | Difficulty: Medium
# DSA Tracker | Topics: Hash Table, String, Sliding Window
# DSA Tracker | Runtime: 191 ms — beats 64.20% of submissions
# DSA Tracker | Memory: 19.9 MB — beats 29.59% of submissions

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength
