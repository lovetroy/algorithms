class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


# solution of traverse
def reverse_list(head):
    pre, cur, = None, head
    while cur:
        cur.next, pre, cur = pre, cur, cur.next
    return pre


# solution of recursive
def reverse_list(head):
    if not head or not head.next:
        return head
    next = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return next


# generate linked list
def gen_list(pre_node, cur_num, end_num):
    cur_node = Node(cur_num)
    if cur_num == end_num:
        cur_node.next = None
    else:
        if pre_node:
            pre_node.next = cur_node
        cur_node.next = gen_list(cur_node, cur_num + 1, end_num)
    return cur_node


# print linked list
def print_list(cur):
    while (cur):
        print(cur.val)
        cur = cur.next


node = gen_list(None, 0, 5)
print_list(node)
node = reverse_list(node)
print_list(node)
