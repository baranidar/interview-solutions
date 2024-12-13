def count_word_frequency(sentence):
  words = sentence.split()
  if len(words) == 0:
      return {}
  output = {}
  for i in words:
      if i in output:
          val = output[i]
          output[i] = val + 1
      else:
          output[i] = 1
  return output
