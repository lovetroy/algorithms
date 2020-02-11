from util import tree_util as util


def max_depth(root):
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1


def max_depth(root):
    stack = []
    depth = 0
    if root is not None:
        stack.append((1, root))
    while stack:
        current_depth, root = stack.pop()
        if root is not None:
            depth = max(depth, current_depth)
            stack.append((current_depth + 1, root.left))
            stack.append((current_depth + 1, root.right))
    return depth


root = util.TreeNode(0,
                     util.TreeNode(1),
                     util.TreeNode(2,
                                   util.TreeNode(3)))

print(max_depth(root))
