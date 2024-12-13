def k_frequent_elements(lst, k):
  my_dict = {}
  # create a hash map
  for index, item in enumerate(lst):
      # print(index, item, my_dict)
      if item in my_dict:
          item_count = my_dict[item]
          item_count += 1
          my_dict[item] = item_count
      else:
          my_dict[item] = 1
  print(my_dict)
  #create a reverse hash
  reverse_hash = {}
  
  for item, value in my_dict.items():
      if value in reverse_hash:
        new_val = reverse_hash[value]
        new_val.append(item)
        reverse_hash[value] = new_val
      else:
        reverse_hash[value] = [item]
  
  print(reverse_hash)
  
  k_frequent_count = 0
  K_frequent_items = []

  for i in range(len(lst),-1,-1):
      if i in reverse_hash:
          for j in reverse_hash[i]:
              if k_frequent_count < k:
                  k_frequent_count += 1
                  K_frequent_items.append(j)
  return(K_frequent_items)
output = k_frequent_elements([5,6,6,7,5,8,9],6)
print(output)
