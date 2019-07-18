class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


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
