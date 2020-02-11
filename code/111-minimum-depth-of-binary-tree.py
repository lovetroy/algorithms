from util import tree_util as util


def min_depth(root):
    if not root:
        return 0
    if not root.left:
        return min_depth(root.right)
    if not root.right:
        return min_depth(root.left)
    return min(min_depth(root.left), min_depth(root.right)) + 1


from collections import deque


def min_depth(root):
    if not root:
        return 0
    else:
        node_deque = deque([(1, root), ])

    while node_deque:
        depth, root = node_deque.popleft()
        print(root.val)
        children = [root.left, root.right]
        if not any(children):
            return depth
        for c in children:
            if c:
                node_deque.append((depth + 1, c))


root = util.TreeNode(0,
                     util.TreeNode(1,util.TreeNode(4,
                                                   util.TreeNode(5))),
                     util.TreeNode(2,
                                   util.TreeNode(3)))

print(min_depth(root))
