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
def bubble_sort(unsorted_list, unsorted_list_count):
    if unsorted_list_count != 0:
        for first_element_index, first_element in enumerate(unsorted_list):
            next_element_index = first_element_index + 1
            if next_element_index < len(unsorted_list):
                if unsorted_list[next_element_index] < unsorted_list[first_element_index]:
                    temp = unsorted_list[next_element_index]
                    unsorted_list[next_element_index] = unsorted_list[first_element_index]
                    unsorted_list[first_element_index] = temp
        bubble_sort(unsorted_list,unsorted_list_count-1)
    return unsorted_list
        


orig_list = [10,12,3,4,2,6,15,23,2]
sorted_list = bubble_sort(orig_list, len(orig_list))
print(sorted_list)


