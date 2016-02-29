# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """


if __name__ == "__main__":
    tree0 = ListNode(0)
    tree1 = ListNode(4)
    tree2 = ListNode(7)
    tree3 = ListNode(3)
    tree4 = ListNode(2)
    tree5 = ListNode(-1)
    tree6 = ListNode(9)
    tree0.next = tree1
    tree1.next = tree3
    tree3.next = tree5
    tree5.next = tree6

    print(str(Solution().deleteNode(tree0)))
