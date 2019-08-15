class TreeNode(object):
    def __init__(self, val=None, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right


import util.tree_util as util


def is_valid_bst(root):
    nodes = pre_order(root)
    pre_val = None
    for node in nodes:
        if pre_val == None:
            pre_val = node.val
            continue
        print(pre_val, node.val)
        if not node.val > pre_val:
            return False
        pre_val = node.val
    return True


def pre_order(node):
    if not node:
        return []
    return pre_order(node.left) + [node] + pre_order(node.right)


root = util.TreeNode(5)
root.left = util.TreeNode(3)
root.right = util.TreeNode(7)

root.left.left = util.TreeNode(2)
root.left.right = util.TreeNode(4)

root.right.left = util.TreeNode(6)
root.right.right = util.TreeNode(8)

# nodes=pre_order(root)
# for node in nodes:
#     print(node.val)

print(is_valid_bst(root))
