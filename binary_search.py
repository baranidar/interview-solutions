def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  
        end_time = time.time()
        print(f"{func.__name__} took {round((end_time-start_time)*1000,4)} ms to run this search")
        return result
    return wrapper


@timer
def find_element_in_list(search_list, search_element):
    for index, element in enumerate(search_list):
        if element == search_element:
            return index
    return -1

@timer
def binary_search(search_list, search_element):
    left_index = 0
    right_index = len(search_list) - 1
    mid_index = 0
    mid_number = search_list[mid_index]
    
    while left_index <= right_index:
        mid_index = (right_index + left_index) // 2
        mid_number = search_list[mid_index]
        if mid_number == search_element:
            return mid_index

        if search_element < mid_number:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1
            
    return -1

@timer
def binary_search_recursive(search_list, search_element, left_index, right_index):
    if left_index <= right_index:
        mid_index = (right_index + left_index) // 2
        mid_number = search_list[mid_index]
        print(left_index, mid_index, right_index, mid_number)
        if mid_number == search_element:
            print("I was here")
            return mid_index

        if search_element < mid_number:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1
    return binary_search_recursive(search_list, search_element, left_index, right_index)

search_list = [i for i in range(1000001)]
search_element = 726985
position = find_element_in_list(search_list, search_element)
print (f"Element was found at position {position}")
position = binary_search(search_list, search_element)
print (f"Element was found at position {position}")
position = binary_search_recursive(search_list, search_element, 0, len(search_list))
print (f"Element was found at position {position}")



