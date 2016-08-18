
import random


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.i = 0
        while head:
            head = head.next
            self.i += 1

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        h = self.head
        t = random.randint(0, self.i - 1)
        print t
        while t:
            if h.next:
                h = h.next
            else:
                h = self.head
            t -= 1
        return h.val


if __name__ == '__main__':
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
    print(Solution(tree0).getRandom())


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
