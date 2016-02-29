# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.dep(root)

    def dep(self, root, l=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        i = 0
        j = 0
        if root: # and root.val:
            l += 1
            if root.left:
                i = self.dep(root.left, l)
            if root.right:
                j = self.dep(root.right, l)
        return max(l, i, j)


if __name__ == "__main__":
    tree0 = TreeNode(0)
    # tree1 = TreeNode(4)
    # tree2 = TreeNode(7)
    # tree3 = TreeNode(3)
    # tree4 = TreeNode(2)
    # tree5 = TreeNode(-1)
    # tree6 = TreeNode(9)
    # tree0.left = tree1
    # tree0.right = tree2
    # tree1.left = tree3
    # tree2.left = tree4
    # tree3.left = tree5
    # tree4.left = tree6

    print(str(Solution().maxDepth(tree0)))
