from collections import deque
def find_letter_case_string_permutations(str1):
  permutations = []
  queue = deque()
  queue.append("")
  for i in range(len(str1)):
    char = str1[i]
    n = len(queue)
    for _ in range(n):
      currentPermutation = queue.popleft()
      for j in range(2):
        if j == 0:
          newPermutation = str(currentPermutation)
          newPermutation = newPermutation + char
        else:
          newPermutation = str(currentPermutation)
          if char.isalpha():
            newPermutation = newPermutation + char.upper()
          else:
            break
        
        if len(newPermutation) == len(str1):
          permutations.append(newPermutation)
        else:
          queue.append(newPermutation)
      
  return permutations


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))

main()



def find_letter_case_string_permutations_2(str1):
  permutations = []
  permutations.append(str1)
  for i in range(len(str1)):
    if str1[i].isalpha():  # only process characters, skip digits
      # we will take all existing permutations and change the letter case appropriately
      n = len(permutations)
      for j in range(n):
        chs = list(permutations[j])
        # if the current character is in upper case, change it to lower case or vice versa
        chs[i] = chs[i].swapcase()
        permutations.append(''.join(chs))

  return permutations



def main2():
  print("String permutations are: " +
        str(find_letter_case_string_permutations_2("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations_2("ab7c")))

main2()