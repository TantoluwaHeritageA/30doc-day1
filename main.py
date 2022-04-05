def new_list():
      array = []
  n = int(input("enter number of elements: "))
  for i in range(n):
    array.append(input("Enter elements now: "))
    new_arr = set(array)
  print(new_arr)
new_list()