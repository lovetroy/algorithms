import util.linked_list_util as util


def reverse_between(head, m, n):
    cur_index = 0
    start, cur = None, head
    while cur_index < m:
        start, cur = cur, cur.next
        cur_index += 1
    pre, end = start, None
    while cur and cur_index < n + 1:
        if pre == start:
            pre, cur = cur, cur.next
        else:
            cur.next, pre, cur = pre, cur, cur.next
        cur_index += 1
    start.next.next = cur
    start.next = pre
    return head


node_input = util.gen_list(None, 0, 5)
util.print_list(node_input)
node_input = reverse_between(node_input, 2, 4)
util.print_list(node_input)
