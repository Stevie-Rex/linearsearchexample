def LinearSearch(input_list: list, element: int):
  list_len = len(input_list)
  for i in range(list_len):
    if input_list[i] == element:
      return i
  return -1




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  myList = [1, 23, 45, 23, 34, 56, 12, 45, 67, 24]
  print("Given list is:", myList)

  result = LinearSearch(myList, 12)

  print("Data found is", result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
