def merge_two_sorted_lists(list1, list2):
    sorted_list = []
    if len(list1) == 0:
        return sorted_list + list2
    if len(list2) == 0:
        return sorted_list + list1 
    i = 0
    j = 0
    total_len = len(list1) + len(list2)
    while i + j < total_len and len(list1) + len(list2) != 1:
        
        print(i,j, sorted_list, list1, list2)
        if list1[0] < list2[0]:
            sorted_list.append(list1[0])
            i += 1
            list1 = list1[1:]
        else:
            sorted_list.append(list2[0])
            j += 1
            list2 = list2[1:]
    if len(list1) == 1:
        sorted_list.append(list1[0])
    else:
        sorted_list.append(list2[0])
    return sorted_list
