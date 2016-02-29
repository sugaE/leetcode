# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            if not p.left and not p.left and not p.right and not q.right:
                return True
            if p.left and q.left:
                if self.isSameTree(p.left, q.left):
                    if p.right and q.right:
                        if self.isSameTree(p.right, q.right):
                            return True
                        else:
                            return False
                else:
                    return False
        return False¡¤


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

    print(Solution().isSameTree(tree0, tree0))
