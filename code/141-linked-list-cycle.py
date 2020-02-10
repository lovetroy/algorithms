import util.linked_list_util as util


def has_cycle(head):
    nodes = set()
    while head:
        if head in nodes:
            return True
        nodes.add(head)
        head = head.next
    return False


def has_cycle(head):
    if not head:
        return False
    slow, fast = head, head.next
    while slow and fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False


node_input = util.gen_list(None, 0, 5)
node_input.next.next.next.next.next = node_input
print(has_cycle(node_input))
