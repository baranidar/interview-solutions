#find duplicates in O(n) and list in same order


def duplicates(lst):
    already_checked = set()
    duplicates =  []
    for item in lst:
        if item in already_checked and item not in duplicates:
            duplicates.append(item)
        else:
            already_checked.add(item)
    return duplicates         

output = duplicates([4,3,6,3,4,8,4,5])
print(output)
