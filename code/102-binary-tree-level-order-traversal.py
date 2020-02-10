import collections
from util import tree_util as util


def level_order(root):
    if not root:
        return []

    res = []
    queue = collections.deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        level_vals = []
        for _ in range(level_size):
            node = queue.popleft()
            level_vals.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level_vals)
    return res


def level_order(root):
    def dfs(node, level):
        if not node: return

        if len(res) < level + 1:
            res.append([])

        res[level].append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    if not root:
        return []
    res = []
    dfs(root, 0)
    return res


root = util.TreeNode(3,
                     util.TreeNode(9),
                     util.TreeNode(20,
                                   util.TreeNode(15),
                                   util.TreeNode(7)))

print(level_order(root))
