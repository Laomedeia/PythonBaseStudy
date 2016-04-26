__author__ = 'neptune'
from AddTwoNumbers import *
if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(2)
    l11 = ListNode(4)
    l12 = ListNode(3)
    l1.next = l11
    l11.next = l12
    l2 = ListNode(5)
    l21 = ListNode(6)
    l22 = ListNode(4)
    l2.next = l21
    l21.next = l22
    result = solution.addTwoNumbers(l1, l2)
    print(result)
