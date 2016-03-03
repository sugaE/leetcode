# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.func(root, [])

    def func(self, root, re):
        '''
        :type root: TreeNode
        :rtype: List[int]
        '''
        if root and root.val is not None:
            re.append(root.val)
            self.func(root.left, re)
            self.func(root.right, re)
        return re


if __name__ == "__main__":
    tree0 = TreeNode(0)
    tree1 = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    tree4 = TreeNode(4)
    tree5 = TreeNode(5)
    tree6 = TreeNode(6)
    tree0.left = tree1
    tree0.right = tree2
    tree1.left = tree3
    tree2.left = tree4
    tree3.left = tree5
    tree3.right = tree6

    print(str(Solution().preorderTraversal(tree0)))
