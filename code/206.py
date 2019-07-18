import util.linked_list_util as util


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


node_input = util.gen_list(None, 0, 5)
util.print_list(node_input)
node_input = reverse_list(node_input)
util.print_list(node_input)
