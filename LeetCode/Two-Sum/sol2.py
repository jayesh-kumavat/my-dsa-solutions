# DSA Tracker | Problem: https://leetcode.com/problems/two-sum/
# DSA Tracker | Language: Python3
# DSA Tracker | Difficulty: Easy
# DSA Tracker | Topics: Array, Hash Table
# DSA Tracker | Runtime: 3 ms — beats 53.56% of submissions
# DSA Tracker | Memory: 20.4 MB — beats 41.98% of submissions

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found
