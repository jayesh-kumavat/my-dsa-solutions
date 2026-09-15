# DSA Tracker | Problem: https://leetcode.com/problems/add-two-numbers/
# DSA Tracker | Language: Python3
# DSA Tracker | Difficulty: Medium
# DSA Tracker | Topics: Linked List, Math, Recursion
# DSA Tracker | Runtime: 0 ms — beats 100.00% of submissions
# DSA Tracker | Memory: 19.3 MB — beats 42.62% of submissions

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        res = dummy

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
        
        return res.next
