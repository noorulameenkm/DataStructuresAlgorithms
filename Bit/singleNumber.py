def find_single_number(arr):
  # TODO: Write your code here
  num = arr[0]
  for i in range(1, len(arr)):
    num = num ^ arr[i]
  
  return num

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()