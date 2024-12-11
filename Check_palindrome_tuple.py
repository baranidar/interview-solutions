def is_palindromic_tuple(tup):
  if tup[::1] == tup[::-1]:
      return True
  else:
      return False
