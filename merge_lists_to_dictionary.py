def merge_lists_to_dictionary(keys, values):
  if len(keys) != len(values):
      return False
  output = {}
  i = 0
  while i < len(keys):
      output[keys[i]]  = values[i]
      i += 1
  return output
