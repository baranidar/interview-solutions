def rotate_list(lst, k):
  length  = len(lst)
  if length == 0:
      return []
  output = [0] * 5
  i = 0
  while i < len(lst):
      pos = i
      pos += k
      if pos > length - 1:
          pos = pos % length
      print(pos, i)
      output[pos] = lst[i]
      i += 1
  return output
