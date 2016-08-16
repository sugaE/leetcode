# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.right, root.left = root.left, root.right
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root


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

    print(str(Solution().invertTree(tree0)))
