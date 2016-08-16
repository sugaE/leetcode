# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail, p, i = head, head, 1
        while tail and tail.next:
            tail = tail.next
            i += 1
        while p and i >= 2:
            t = p.next
            tail.next = t
            tail = tail.next
            if t:
                p.next = t.next
                t.next = None
            p = p.next
            i -= 2
            printtree(head)
            print i
        return head


def printtree(tree):
    s = ''
    while tree:
        s += str(tree.val) + ' -> '
        tree = tree.next
    print s


if __name__ == '__main__':
    tree0 = ListNode(0)
    tree1 = ListNode(1)
    tree2 = ListNode(2)
    tree3 = ListNode(3)
    tree4 = ListNode(4)
    tree5 = ListNode(5)
    tree6 = ListNode(6)
    tree7 = ListNode(7)
    tree8 = ListNode(8)
    tree0.next = tree1
    tree1.next = tree2
    tree2.next = tree3
    tree3.next = tree4
    # tree4.next = tree5
    # tree5.next = tree6
    # tree6.next = tree7
    # tree7.next = tree8

    printtree(tree0)
    printtree(Solution().oddEvenList(tree0))
