
# slow fast two pointer approach
# https://leetcode.com/problems/linked-list-cycle/
def hasCycle(head) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
