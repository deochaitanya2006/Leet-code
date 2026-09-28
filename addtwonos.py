class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = (0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                num1 = l1.val
            else:
                num1 = 0

            if l2:
                num2 = l2.val
            else:
                num2 = 0
            total = num1 + num2 + carry
            carry = total // 10
            digit = total % 10
            current.next = (digit)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next