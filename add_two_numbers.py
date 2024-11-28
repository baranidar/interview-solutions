# Add two numbers stored in linked lists and return their sum as a linked list in the reverse order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None  
    
    def add_item(self, data):
        node = ListNode(val=data)
        if self.head == None:           
            self.head = node
            return
        
        current_node = self.head
        while current_node:
            last_node = current_node
            current_node = current_node.next
        last_node.next = node

    def return_linked_list(self):
        current_node = self.head
        return current_node

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str = ""
        while l1:
            l1_str += str(l1.val)
            l1 = l1.next
        l1_str = l1_str[::-1]
        l1_int = int(l1_str)
        l2_str = ""
        while l2:
            l2_str += str(l2.val)
            l2 = l2.next
        l2_str = l2_str[::-1]
        l2_int = int(l2_str)
        add_str = str(l1_int + l2_int)[::-1]
        final_list = list(add_str)
        print(final_list)
        ll = Linked_List()
        for item in final_list:
            ll.add_item(int(item))
        result  = ll.return_linked_list()
        return result


