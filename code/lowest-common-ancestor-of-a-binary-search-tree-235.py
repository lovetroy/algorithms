# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import util.tree_util as util


def lowest_common_ancestor(root, p, q):
    if p < root.val > q:
        return lowest_common_ancestor(root.left, p, q)
    if p > root.val < q:
        return lowest_common_ancestor(root.right, p, q)
    return root


def lowest_common_ancestor(root, p, q):
    while True:
        if p < root.val > q:
            root = root.left
        elif p > root.val < q:
            root = root.right
        else:
            return root


root = util.TreeNode(5)
root.left = util.TreeNode(2)
root.right = util.TreeNode(8)
root.left.right = util.TreeNode(3)
root.left.right.right = util.TreeNode(4)
node = lowest_common_ancestor(root, 2, 8)
print(node.val)
