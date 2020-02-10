# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import util.tree_util as util
from collections import deque


def lowest_common_ancestor(root, p, q):
    if not root or root.val == p or root.val == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if not left:
        return right
    if not right:
        return left
    return root


def lowest_common_ancestor(root, p, q):
    if not root:
        return False
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    mid = root == p or root == q
    # If any two of the three flags left, right or mid become True.
    if mid + left + right >= 2:
        return root
    # Return True if either of the three bool values is True.
    return mid or left or right


def lowest_common_ancestor(root, p, q):
    # Stack for tree traversal
    stack = [root]
    # Dictionary for parent pointers
    parent = {root.val: None}

    # Iterate until we find both the nodes p and q
    while p not in parent or q not in parent:
        node = stack.pop()
        # While traversing the tree, keep saving the parent pointers.
        if node.left:
            parent[node.left.val] = node.val
            stack.append(node.left)
        if node.right:
            parent[node.right.val] = node.val
            stack.append(node.right)

    # Ancestors set() for node p.
    ancestors = set()
    # Process all ancestors for node p using parent pointers.
    while p:
        ancestors.add(p)
        p = parent[p]

    # The first ancestor of q which appears in
    # p's ancestor set() is their lowest common ancestor.
    while q not in ancestors:
        q = parent[q]
    return q


# [3,5,1,6,2,0,8,null,null,7,4]
root = util.TreeNode(3)
root.left = util.TreeNode(5)
root.right = util.TreeNode(1)
root.left.right = util.TreeNode(2)
root.left.right.right = util.TreeNode(4)
node = lowest_common_ancestor(root, 2, 4)
print(node)
