    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = merged_list_head = ListNode() 

        while list1 and list2:
            if list1.val < list2.val:
                merged_list.next = list1
                list1 = list1.next
                merged_list = merged_list.next
            else:
                merged_list.next = list2
                list2 = list2.next
                merged_list = merged_list.next

        if list1:
            merged_list.next = list1

        if list2:
            merged_list.next = list2
        
        return merged_list_head.next
