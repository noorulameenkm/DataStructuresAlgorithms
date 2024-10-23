def backspace_compare(str1, str2):
  index1 = len(str1) - 1
  index2 = len(str2) - 1
  while index1 >= 0 and index2 >= 0:
    i1 = get_next_valid_char(str1, index1)
    i2 = get_next_valid_char(str2, index2)

    if i1 < 0 and i2 < 0:
      return True
    if i1 < 0 or i2 < 0:
      return False
    
    if str1[i1] != str2[i2]:
      return False


    index1 = i1 - 1
    index2 = i2 - 1

  if index1 < 0 and index2 < 0:
    return True

  if index1 < 0:
    return get_next_valid_char(str2, index2) == -1

  if index2 < 0:
    return get_next_valid_char(str1, index1) == -1



def get_next_valid_char(str_, index):
  backspace_count = 0
  while index >= 0:
    if str_[index] == '#':
      backspace_count += 1
    elif backspace_count > 0:
      backspace_count -= 1
    else:
      break
    
    index -= 1
 
  return index



def main():
  print(backspace_compare("xy#z", "xzz#"))
  print(backspace_compare("xy#z", "xyz#"))
  print(backspace_compare("xp#", "xyz##"))
  print(backspace_compare("xywrrmp", "xywrrmu#p"))
  print(backspace_compare("abc###", ""))
  print(backspace_compare("ac##b", "b"))


main()