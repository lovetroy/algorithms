import util.tree_util as util


# 解法1
def is_valid_bst(root):
    inorder = in_order(root)
    return inorder == list(sorted(set(inorder)))


def in_order(root):
    if not root:
        return []
    return in_order(root.left) + [root.val] + in_order(root.right)


# 解法2
class Solution:
    def is_valid_bst(self, root):
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if not root:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)


# 解法3
def is_valid_bst(root):
    return helper(root, None, None)


def helper(root, min, max):
    if not root:
        return True
    if min is not None and root.val <= min:
        return False
    if max is not None and root.val >= max:
        return False
    return helper(root.left, min, root.val) and helper(root.right, root.val, max)


root = util.TreeNode(0)
# root.left = util.TreeNode(3)
root.right = util.TreeNode(-1)
#
# root.left.left = util.TreeNode(2)
# root.left.right = util.TreeNode(4)
#
# root.right.left = util.TreeNode(6)
# root.right.right = util.TreeNode(8)

# nodes=pre_order(root)
# for node in nodes:
#     print(node.val)

print(is_valid_bst(root))
