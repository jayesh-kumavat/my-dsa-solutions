// DSA Tracker | Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
// DSA Tracker | Language: C++
// DSA Tracker | Difficulty: Medium
// DSA Tracker | Topics: Hash Table, String, Sliding Window
// DSA Tracker | Runtime: 51 ms — beats 48.05% of submissions
// DSA Tracker | Memory: 19.1 MB — beats 59.69% of submissions

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        int maxLength = 0;
        unordered_map<char, int> charMap;
        int left = 0;
        
        for (int right = 0; right < n; right++) {
            if (charMap.count(s[right]) == 0 || charMap[s[right]] < left) {
                charMap[s[right]] = right;
                maxLength = max(maxLength, right - left + 1);
            } else {
                left = charMap[s[right]] + 1;
                charMap[s[right]] = right;
            }
        }
        
        return maxLength;
    }
};
