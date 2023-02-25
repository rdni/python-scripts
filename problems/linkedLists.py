class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next =next

def toList(head):
    if not head:
        return []
    if not head.next:
        return [head.val]
    if isinstance(head.next, ListNode):
        return [head.val] + toList(head.next)
    
def toLinkedList(l):
    if not l:
        return None
    else:
        return ListNode(l[0], next=toLinkedList(l[1:]))

def reverseList(head):
    if not head:
        return None
    if not head.next:
        return head
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

print(reverseList(ListNode(1, next=ListNode(5))).val)
print(toList(reverseList(ListNode(1, next=ListNode(5)))))
print(toList(toLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))