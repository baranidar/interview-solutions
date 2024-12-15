def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None :
        return head
    c = head
    p = None
    n = c.next
    while c:
        n = c.next
        c.next = p
        p = c
        c = n 
    c = p
    return c
