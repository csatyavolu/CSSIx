def longest_word(w1, w2, w3):
  l1 = len(w1)
  l2 = len(w2)
  l3 = len(w3)
  if l1 > l2 and l1 > l3:
    return w1
  elif l2 > l1 and l2 > l3:
    return w2
  else:
    return w3

print(longest_word("a","aa","aaa"))
