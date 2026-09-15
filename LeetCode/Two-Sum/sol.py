# DSA Tracker | Problem: https://leetcode.com/problems/two-sum/
# DSA Tracker | Language: Python3
# DSA Tracker | Difficulty: Easy
# DSA Tracker | Topics: Array, Hash Table
# DSA Tracker | Runtime: 3 ms — beats 53.56% of submissions
# DSA Tracker | Memory: 20.6 MB — beats 7.37% of submissions

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []
