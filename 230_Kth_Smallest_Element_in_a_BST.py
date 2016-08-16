# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        node = root
        while node and node.left:
            node = node.left
        print node.val

if __name__ == "__main__":
    tree0 = TreeNode(1)
    tree1 = TreeNode(2)
    tree2 = TreeNode(3)
    tree3 = TreeNode(4)
    tree4 = TreeNode(5)

    tree00 = TreeNode(1)
    tree11 = TreeNode(2)
    tree22 = TreeNode(3)
    tree33 = TreeNode(4)
    tree44 = TreeNode(5)
    # tree5 = TreeNode(-1)
    # tree6 = TreeNode(9)
    tree0.left = tree1
    tree0.right = tree2
    tree1.left = tree3
    tree1.right = tree4

    tree00.left = tree11
    tree00.right = tree22
    tree11.left = tree33
    tree22.left = tree44

    # print(Solution().kthSmallest(None, None))
    print(Solution().kthSmallest(tree0, tree0))
    print(Solution().kthSmallest(tree0, tree00))
