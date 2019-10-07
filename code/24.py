from util import linked_list_util as util


def swap_pairs(head):
    pre, pre.next = util.Node(0), head
    tmp = pre
    while tmp.next and tmp.next.next:
        a, b = tmp.next, tmp.next.next
        tmp.next = b
        a.next = b.next
        b.next = a
        tmp = a
    return pre.next


def swap_pairs(head):
    if not head or not head.next:
        return head
    next = head.next
    head.next = swap_pairs(next.next)
    next.next = head
    return next


node = util.gen_list(None, 1, 4)
node = swap_pairs(node)
util.print_list(node)
